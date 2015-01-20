import os
import shutil
import tempfile

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.files.storage import FileSystemStorage

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from .. import views


class FunctionalTests(StaticLiveServerTestCase):
    """Iteractive tests with selenium."""

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.PhantomJS()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self._orig_storage = views.storage
        views.storage = FileSystemStorage(self.temp_dir)
        self.username = 'test'
        self.password = 'test'
        User.objects.create_user(self.username, '', self.password)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)
        views.storage = self._orig_storage

    def test_show_login(self):
        """The login should be shown on page load."""

        self.browser.get(self.live_server_url)
        form = self.browser.find_element_by_id('login')
        upload = self.browser.find_element_by_id('upload')
        self.assertTrue(form.is_displayed(), 'Login form should be visible.')
        self.assertFalse(upload.is_displayed(), 'Upload area should not be visible.')

    def login(self, username, password):
        """Helper for login form submission."""

        self.browser.get(self.live_server_url)
        form = self.browser.find_element_by_id('login')
        username_input = form.find_element_by_name('username')
        username_input.send_keys(username)
        password_input = form.find_element_by_name('password')
        password_input.send_keys(password)
        form.submit()

    def test_login(self):
        """Submit the login form with a valid login."""

        self.login(self.username, self.password)
        WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, 'upload')))
        form = self.browser.find_element_by_id('login')
        self.assertFalse(form.is_displayed(), 'Login form should no longer be visible.')

    def test_invalid_login(self):
        """Submit the login form with an invalid login."""

        self.login(self.username, self.password[1:])
        error = WebDriverWait(self.browser, 5).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, 'error')))
        self.assertEqual('Invalid username/password', error.text)
        form = self.browser.find_element_by_id('login')
        self.assertTrue(form.is_displayed(), 'Login form should still be visible.')

    def test_browse_files(self):
        """Browse existing uploads."""

        _, test_file = tempfile.mkstemp(dir=self.temp_dir)
        self.login(self.username, self.password)
        element = WebDriverWait(self.browser, 5).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'file')))
        self.assertIn(os.path.basename(test_file), element.text)

    def test_file_delete(self):
        """Delete uploaded file."""

        _, test_file = tempfile.mkstemp(dir=self.temp_dir)
        self.login(self.username, self.password)
        element = WebDriverWait(self.browser, 5).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'file')))
        element.find_element_by_class_name('delete').click()
        self.browser.implicitly_wait(1)
        with self.assertRaises(NoSuchElementException):
            self.browser.find_element_by_class_name('file')
        self.assertFalse(os.path.exists(test_file))

    def upload(self, filepath):
        # Create file input for fake drag and drop
        self.browser.execute_script('''
            input = $('<input>', {id: 'seleniumUpload', type: 'file'}).appendTo('body');
        ''');
        self.browser.find_element_by_id('seleniumUpload').send_keys(filepath)
        # Fake a file drag and drop event
        self.browser.execute_script('''
            event = $.Event('drop');
            event.originalEvent = {
                dataTransfer: {files: input.get(0).files}
            };
            $('#upload').trigger(event);
        ''');

    def test_file_upload(self):
        """Drag and drop a new file upload."""

        self.login(self.username, self.password)
        _, test_file = tempfile.mkstemp()
        with open(test_file, 'w') as f:
            f.write('XXX')
        self.upload(test_file)
        element = WebDriverWait(self.browser, 5).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'file')))
        self.assertIn(os.path.basename(test_file), element.text)

    def test_invalid_file(self):
        """Drag and drop a new file upload."""

        self.login(self.username, self.password)
        _, test_file = tempfile.mkstemp()
        self.upload(test_file)
        element = WebDriverWait(self.browser, 5).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, 'error')))
        self.assertEqual('The submitted file is empty.', element.text)