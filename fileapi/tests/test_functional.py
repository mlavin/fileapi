from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


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

    def test_show_login(self):
        """The login should be shown on page load."""

        self.browser.get(self.live_server_url)
        form = self.browser.find_element_by_id('login')
        upload = self.browser.find_element_by_id('upload')
        self.assertTrue(form.is_displayed(), 'Login form should be visible.')
        self.assertFalse(upload.is_displayed(), 'Upload area should not be visible.')
