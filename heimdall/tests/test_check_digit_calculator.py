import unittest

from heimdall.check_digit_calculator import CalculateAgencyCheckDigit
from heimdall.tests.data import BANCO_DO_BRASIL


class TestCheckDigitCalculator(unittest.TestCase):

    def test_calculate_check_digit_agency_bb(self):
        for bank_data in BANCO_DO_BRASIL['valid_combinations']:
            agency = bank_data['branch'],
            agency = agency[0]
            digit = bank_data['branch_digit']
            digit_calculated = CalculateAgencyCheckDigit(agency).calculate_check_digit_agency_bb()
            assert digit_calculated == digit

if __name__ == '__main__':
    unittest.main()
