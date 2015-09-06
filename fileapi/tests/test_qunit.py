import os

from django.conf import settings
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test.utils import modify_settings

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


@modify_settings(STATICFILES_DIRS={
    'append': os.path.join(os.path.dirname(__file__), 'static')})
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

    def test_qunit(self):
        """Load the QUnit tests and check for failures."""

        self.browser.get(self.live_server_url + settings.STATIC_URL + 'index.html')
        results = WebDriverWait(self.browser, 5).until(
            expected_conditions.visibility_of_element_located((By.ID, 'qunit-testresult')))
        total = int(results.find_element_by_class_name('total').text)
        failed = int(results.find_element_by_class_name('failed').text)
        self.assertTrue(total and not failed, results.text)
