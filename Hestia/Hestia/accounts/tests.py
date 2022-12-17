from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError

user = get_user_model()


class ProfileModelTests(TestCase):

    def test_profile_save__when_phone_num_is_valid__expect_correct_result(self):
        profile = user(
            username='Rado',
            phone_number='0888899999',
            email='rado@gmail.com',
            password='12aw2@',
            first_name='Radoslav',
            last_name='Grigorov',
        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_phone_num_is_11_digits__expect_validation_error(self):
        profile = user(
            username='Rado',
            phone_number='08888999999',
            email='rado@gmail.com',
            password='12aw2@',
            first_name='Radoslav',
            last_name='Grigorov',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save__when_phone_num_is_8_digits__expect_validation_error(self):
        profile = user(
            username='Rado',
            phone_number='08888999',
            email='rado@gmail.com',
            password='12aw2@',
            first_name='Radoslav',
            last_name='Grigorov',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save__when_phone_num_has_non_digit_char__expect_validation_error(self):
        profile = user(
            username='Rado',
            phone_number='088889s99',
            email='rado@gmail.com',
            password='12aw2@',
            first_name='Radoslav',
            last_name='Grigorov',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)



