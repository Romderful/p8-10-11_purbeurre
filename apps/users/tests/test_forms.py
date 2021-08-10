"""Test the forms."""


import time
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from apps.users.forms import SignupForm
from django.test import LiveServerTestCase


class TestForms(TestCase):
    """Test the forms."""

    def test_sign_up_form_valid_data(self):
        """Test sign up form valid data."""
        form = SignupForm(
            data={
                "email": "test@gmail.com",
                "username": "test",
                "password1": "Testtest123",
                "password2": "Testtest123",
            }
        )
        self.assertTrue(form.is_valid())

    def test_sign_up_form_no_data(self):
        """Test sign up form no data."""
        form = SignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class MySeleniumTests(LiveServerTestCase):
    """Selenium tests."""

    @classmethod
    def setUpClass(cls):
        """Set up."""
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)
        user: User = get_user_model()  # type: ignore
        user.objects.create_user(  # type: ignore
            username="test", email="test@gmail.com", password="Secret"
        )

    @classmethod
    def tearDownClass(cls):
        """Tear down."""
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        """Sign in test."""
        self.selenium.get("%s%s" % (self.live_server_url, "/users/sign_in"))
        time.sleep(1)
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys("test@gmail.com")
        time.sleep(1)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("Secret")
        time.sleep(1)
        self.selenium.find_element_by_id("sign-in-form").submit()
        time.sleep(1)
        self.selenium.get("%s%s" % (self.live_server_url, "/users/profile"))
        time.sleep(1)
        self.assertIn(member="test@gmail.com", container=self.selenium.page_source)
