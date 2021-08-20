"""Test the forms."""


from apps.accounts.models import CustomUser
from django.test.testcases import TestCase
from apps.accounts.forms import CustomUserCreationForm
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from config import settings


class TestForms(TestCase):
    """Test the forms."""

    def test_signup_form_valid_data(self):
        """Test signup form valid data."""
        form = CustomUserCreationForm(
            data={
                "email": "test@gmail.com",
                "username": "test",
                "password1": "Testtest123",
                "password2": "Testtest123",
            }
        )
        self.assertTrue(form.is_valid())

    def test_signup_form_no_data(self):
        """Test signup form no data."""
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)


class MySeleniumSignInTests(StaticLiveServerTestCase):
    """Selenium tests."""

    @classmethod
    def setUpClass(cls):
        """Set up."""
        super().setUpClass()
        cls.selenium = WebDriver(
            executable_path=str(settings.BASE_DIR / "webdrivers" / "chromedriver")
        )
        cls.selenium.implicitly_wait(10)
        CustomUser.objects.create_user(  # type: ignore
            username="test", email="test@gmail.com", password="Secret"
        )

    @classmethod
    def tearDownClass(cls):
        """Tear down."""
        cls.selenium.quit()
        super().tearDownClass()

    def test_login_and_visit_profile(self):
        """Login test."""
        self.selenium.get("%s%s" % (self.live_server_url, "/accounts/login"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("test@gmail.com")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("Secret")
        self.selenium.find_element_by_id("sign-in-form").submit()
        self.selenium.get("%s%s" % (self.live_server_url, "/accounts/profile"))
        self.assertIn(member="test@gmail.com", container=self.selenium.page_source)
