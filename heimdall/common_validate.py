import re
class CommonValidate:
    @staticmethod
    def agency_is_valid(agency):
        regex = re.compile('^(?!0000)([0-9]{4})$', re.I)
        return bool(regex.match(agency))
    
    @staticmethod
    def agency_digit_is_valid(agency_digit):
        """
        docstring
        """
        regex = re.compile('^[a-zA-Z0-9]{0,1}$', re.I)
        return bool(regex.match(agency_digit))

    @staticmethod
    def account_is_valid(account):
        """
        docstring
        """
        regex = re.compile('^[0-9]{1,12}$', re.I)
        return bool(regex.match(account))
    
    @staticmethod
    def account_digit_is_valid(account_digit):
        """
        docstring
        """
        regex = re.compile('^[a-zA-Z0-9]{1}$', re.I)
        return bool(regex.match(account_digit))
