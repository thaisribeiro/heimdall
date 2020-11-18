import re
from generic_validators import GenericValidators
from common_validate import CommonValidate
from base_validate_error import InvalidAgencyNumber, InvalidDigitAgencyNumber,InvalidAccountNumber, InvalidDigitAccountNumber, InvalidCodeBankP 
from calculate_number_account_agency import CalculateNumberAccount, CalculateNumberAgency
class AccountValidator(CommonValidate):
    def __init__(self, config):
        self.config = config

    def start(self):
        try:
            bank_code = self.config.get('bank_code')
            account_code = self.config.get('account_code')

            switcher = {
                '001': AccountValidator.valid_account_bb,
                '237': AccountValidator.valid_account_bradesco,
                '341': AccountValidator.valid_account_itau,
                '033': AccountValidator.valid_account_santander,
                '745': AccountValidator.valid_account_citibank,
                '399': AccountValidator.valid_account_hsbc,
                '041': AccountValidator.valid_account_banrisul
            }
            
            result = switcher.get(bank_code)()

            if not result:
                return self.valid_account_generic()

            return result
        except Exception:
            print('Erro')
    
    def valid_account_generic(self):
        return {}

    def valid_account_bb(self):
        return {}

    def valid_account_itau(self):
        account = self.config('account')

        if len(account) < 5:
            raise InvalidAccountNumber(5)
        
        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()
        
        account_agency = account + self.config('agency')
        calculate_account = CalculateNumberAccount(account_agency).calculate_number_itau()
        
        if not calculate_account:
            raise InvalidAccountNumber()
        
        return True

    def valid_account_bradesco(self):
        return {}

    def valid_account_santander(self):
        return {}

    def valid_account_citibank(self):
        return {}
    
    def valid_account_banrisul(self):
        return {}
    
    def valid_account_hsbc(self):
        return {}