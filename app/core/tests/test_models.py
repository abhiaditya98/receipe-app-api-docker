"""
Test for Models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):

        email='test@example.com'
        password='password123'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails=[
            ['test1@EXAMPLE.com','test1@example.com'],
            ['test2@Example.com','test2@example.com'],
            ['test3@EXAMPLE.com','test3@example.com'],
            ['test4@example.com','test4@example.com'],
        ]
        for email,excepted in sample_emails:
            user= get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, excepted)
    
    def test_new_user_without_email_raises_error(self):
        """Test that creating a user awithout an email raise a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a super user"""
        user=get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

