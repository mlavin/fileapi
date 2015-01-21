import os

from django.conf import settings
from django.contrib.staticfiles import finders, storage
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.utils import override_settings
from django.utils.functional import empty

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@override_settings(STATICFILES_DIRS=(os.path.join(os.path.dirname(__file__), 'static'), ))
class QunitTests(StaticLiveServerTestCase):
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
        # Clear the cache versions of the staticfiles finders and storage
        # See https://code.djangoproject.com/ticket/24197
        storage.staticfiles_storage._wrapped = empty
        finders.get_finder.cache_clear()

    def test_qunit(self):
        """Load the QUnit tests and check for failures."""

        self.browser.get(self.live_server_url + settings.STATIC_URL + 'index.html')
        results = WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, 'qunit-testresult')))
        total = int(results.find_element_by_class_name('total').text)
        failed = int(results.find_element_by_class_name('failed').text)
        self.assertTrue(total and not failed, results.text)
