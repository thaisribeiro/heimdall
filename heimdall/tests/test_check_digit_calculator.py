import unittest

from heimdall.calculate_number_account import CalculateAccount, CalculateAccountCheckDigit
from heimdall.tests.data import BANCO_DO_BRASIL, BRADESCO, BANRISUL, CAIXA_ECONOMICA_FEDERAL, \
    SANTANDER, CITIBANK, ITAU, NUBANK


class TestCheckDigitCalculator(unittest.TestCase):

    def test_calculate_check_digit_agency_bb(self):
        for bank_data in BANCO_DO_BRASIL['valid_combinations']:
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['branch_digit']
            digit_calculated = CalculateAgencyCheckDigit(agency).calculate_check_digit_agency_bb()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_bb(self):
        for bank_data in BANCO_DO_BRASIL['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(config={'account': account }).calculate_check_digit_account_bb()
            assert digit_calculated == digit

    def test_calculate_check_digit_agency_bradesco(self):
        for bank_data in BRADESCO['valid_combinations']:
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['branch_digit']
            digit_calculated = CalculateAgencyCheckDigit(agency).calculate_check_digit_agency_bradesco()
            is_valid = False
            if digit == '0':
                is_valid = (digit_calculated == '0' or digit_calculated == 'P')
            else:
                is_valid = (digit_calculated == digit)

            assert is_valid is True

    def test_calculate_check_digit_account_bradesco(self):
        for bank_data in BRADESCO['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(account, None).calculate_check_digit_account_bradesco()
            is_valid = False
            if digit == '0':
                is_valid = (digit_calculated == '0' or digit_calculated == 'P')
            else:
                is_valid = (digit_calculated == digit)

            assert is_valid is True

    def test_calculate_check_digit_agency_banrisul(self):
        for bank_data in BANRISUL['correct_agency']:
            agency = bank_data[0]
            digit = bank_data[1]
            digit_calculated = CalculateAgencyCheckDigit(agency).calculate_check_digit_agency_banrisul()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_banrisul(self):
        for bank_data in BANRISUL['correct_account']:
            account = bank_data[0]
            digit = bank_data[1]
            digit_calculated = CalculateAccountCheckDigit(config={'account': account }).calculate_check_digit_account_banrisul()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_caixa(self):
        for bank_data in CAIXA_ECONOMICA_FEDERAL['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(config={'account': account, 'agency': agency }).calculate_check_digit_account_caixa()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_santander(self):
        for bank_data in SANTANDER['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(account, agency).calculate_check_digit_account_santander()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_citibank(self):
        for bank_data in CITIBANK['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(account, None).calculate_check_digit_account_citibank()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_itau(self):
        for bank_data in ITAU['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(config={'account': account, 'agency': agency }).calculate_check_digit_account_itau()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_itau(self):
        for bank_data in ITAU['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(account, agency).calculate_check_digit_account_itau()
            assert digit_calculated == digit

    def test_calculate_check_digit_account_nubank(self):
        for bank_data in NUBANK['valid_combinations']:
            account = bank_data['account'],
            account = account[0]
            digit = bank_data['account_digit']
            digit_calculated = CalculateAccountCheckDigit(config={'account': account, 'agency': None }).calculate_check_digit_account_nubank()
            assert digit_calculated == digit

if __name__ == '__main__':
    unittest.main()
