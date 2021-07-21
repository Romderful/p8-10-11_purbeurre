"""Test the forms."""


from django.test.testcases import TestCase
from apps.users.forms import SigninForm, SignupForm


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
        self.assertEquals(len(form.errors), 4)

    def test_sign_in_form_no_data(self):
        """Test sign in form no data."""
        form = SigninForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
