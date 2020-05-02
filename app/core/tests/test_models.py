from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_successful(self):
        """Test creating a new user with an email is successfull"""
        email = 'ajitesh@example.com'
        password = 'ajitesh@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test the email for a new user is normalized"""
        email = "ajitesh@EXAMPLE.IN"
        user = get_user_model().objects.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_invalid(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_super_user(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser('test@example.in', 'test1234')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
