import re
from heimdall.common_validate import CommonValidate
from heimdall.base_validate_error import (InvalidAgencyNumber, InvalidDigitAgencyNumber, InvalidAccountNumber,
                                          InvalidDigitAccountNumber)
from heimdall.check_digit_calculator import CalculateAccountCheckDigit


class AccountValidator(CommonValidate):
    def __init__(self, config):
        self.bank_code = config.get('bank_code')
        self.account = config.get('account')

        regex = re.search('[@_!#$%^&*()<>?/\-.|}{~:]', self.account)
        if regex:
            self.digit_account = self.account[regex.start()+1:len(self.account)]

        if config.get('digit_account'):
            self.digit_account = config.get('digit_account')

    def start(self):
        try:
            switcher = {
                '001': AccountValidator.valid_account_bb,
                '237': AccountValidator.valid_account_bradesco,
                '341': AccountValidator.valid_account_itau,
                '033': AccountValidator.valid_account_santander,
                '745': AccountValidator.valid_account_citibank,
                '041': AccountValidator.valid_account_banrisul,
                '104': AccountValidator.valid_account_caixa,
                '260': AccountValidator.valid_account_nubank
            }

            result = switcher.get(self.bank_code)()

            if not result:
                return self.valid_account_generic()

            return result
        except Exception:
            return False

    def valid_account_generic(self):
        return {}

    def valid_account_bb(self):
        """
          Valida a conta e o dígito verificador do Banco do Brasil
          Tamanho da Conta - 8 Dígitos + 1 DV
        """
        account = self.account

        if len(account) < 9:
            raise InvalidAccountNumber(9)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        check_number_calculate_account = CalculateAccountCheckDigit(
            config={'account': account}).calculate_check_digit_account_bb()

        if not check_number_calculate_account:
            raise InvalidAccountNumber()

        return check_number_calculate_account == self.digit_account.upper()

    def valid_account_itau(self):
        """
          Valida a conta e o dígito verificador do banco Itaú
          Tamanho da Conta - 5 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 6:
            raise InvalidAccountNumber(6)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        account_agency = account + self.config('agency')
        calculate_account = CalculateAccountCheckDigit(
            account_agency).calculate_check_digit_account_itau()

        if not calculate_account:
            raise InvalidAccountNumber()

        return True

    def valid_account_bradesco(self):
        """
          Valida a conta e o dígito verificador do banco Bradesco
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 8:
            raise InvalidAccountNumber(8)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateAccountCheckDigit(
            account).calculate_check_digit_account_bradesco()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_santander(self):
        """
          Valida a conta e o dígito verificador do banco Santander
          Tamanho da Conta - 8 dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 9:
            raise InvalidAccountNumber(9)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateAccountCheckDigit(
            account).calculate_check_digit_account_santander()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_citibank(self):
        """
          Valida a conta e o dígito verificador do banco Banrisul
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 8:
            raise InvalidAccountNumber(8)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateAccountCheckDigit(
            account).calculate_check_digit_account_citibank()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_banrisul(self):
        """
          Valida a conta e o dígito verificador do banco Banrisul
          Tamanho da Conta - 9 Dígitos + 1 DV (sendo os dois primeiros o tipo de conta)
        """
        account = self.config('account')

        if len(account) < 10:
            raise InvalidAccountNumber(10)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateAccountCheckDigit(
            account).calculate_check_digit_account_banrisul()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_caixa(self):
        """
          Valida a conta e o dígito verificador do banco Caixa Econômica Federal
          Tamanho da Conta - 11 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 12:
            raise InvalidAccountNumber(12)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateAccountCheckDigit(
            account).calculate_check_digit_account_caixa()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True

    def valid_account_nubank(self):
        """
          Valida a conta e o dígito verificador do banco Nu Pagamentos (Nubank)
          Tamanho da Conta - 7 Dígitos + 1 DV
        """
        account = self.config('account')

        if len(account) < 8:
            raise InvalidAccountNumber(8)

        result = super().account_is_valid(account)

        if result == False:
            raise InvalidAccountNumber()

        calculate_account = CalculateAccountCheckDigit(
            account).calculate_check_digit_account_nubank()

        if not calculate_account:
            raise InvalidDigitAccountNumber()

        return True
