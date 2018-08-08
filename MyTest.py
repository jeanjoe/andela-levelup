import unittest

import signup

signupClass = signup.SignUp('Manzede', 'Benard', 'manzede@gmail.com')


class TestSignUp(unittest.TestCase):

    def test_name(self):
        self.assertEqual(signupClass.full_name(), 'Manzede Benard')

    def test_email(self):
        self.assertTrue(signupClass.validate_email('manzede@gmail.com'), True)

    def test_valid_phone(self):
        self.assertTrue(signupClass.validate_phone_number('256773969641'), True)


if __name__ == '__main__':
    unittest.main()
