import unittest

import signup

signupClass = signup.SignUp('Manzede', 'Benardfhf', 'manzede@gmail.com')


class TestSignUp(unittest.TestCase):

    def test_name(self):
        self.assertEqual(signupClass.combine_name(), 'Manzede Benard')

    def test_email(self):
        self.assertTrue(signupClass.validate_email('manzedegmail.com'), True)


if __name__ == '__main__':
    unittest.main()
