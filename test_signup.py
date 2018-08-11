import re


class SignUp(object):

    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    def full_name(self):
        fullname = self.first_name + " " + self.last_name
        return fullname

    def phone_number(self):
        return self.phone_number

    def submit(self):
        if self.valid_email(self.email) & self.valid_phone_number(self.phone_number):
            return {'name': self.full_name(), 'email': self.email, 'phone_number': self.phone_number}
        return "Invalid Email address or phone number"

    @staticmethod
    def valid_email(email_address):
        email_reg = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        if not email_reg.match(email_address):
            return False
        else:
            return True

    @staticmethod
    def valid_phone_number(phone_number):
        rule = re.compile(r'(^[+0-9]{1,3})*([0-9]{10,11}$)')
        if not rule.search(phone_number):
            return False
        return True

#
# first_name = input("Enter First name: \t")
# last_name = input("Enter Last name: \t")
# email = input("Enter valid email address: \t")
# phone = input("Enter valid phone number: \t")
#
# signup = SignUp(first_name, last_name, email, phone)
# print(signup.submit())
