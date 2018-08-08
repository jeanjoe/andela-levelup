import re


class SignUp(object):

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def full_name(self):

        fullname = self.first_name + " " + self.last_name

        return fullname

    def phone_number(self):

        return

    def submit(self):

        if self.validate_email(self.email):

            return self.full_name()

        else:
            return "Invalid Email address"

    @staticmethod
    def validate_email(email_address):

        email_reg = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        if not email_reg.match(email_address):

            return False

        else:

            return True
    @staticmethod
    def validate_phone_number(phonenumber):

        rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')

        if not rule.search(phonenumber):
            return False
        else:
            return True

#
# first_name = input("Enter First name: \t")
# last_name = input("Enter Last name: \t")
# email = input("Enter valid email address: \t")
#
# signup = SignUp(first_name, last_name, email)
# print("Output: " + signup.submit())
