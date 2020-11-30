from unittest import TestCase

from heimdall.calculate_number_account import CalculateAccount
from heimdall.tests.data import BANCO_DO_BRASIL, BRADESCO, BANRISUL, CAIXA_ECONOMICA_FEDERAL, SANTANDER, CITIBANK, ITAU, NUBANK


class TestCalculateAccount(TestCase):

    def test_calculate_account_bb_valid(self):
        bank = BANCO_DO_BRASIL['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_bb()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated == accounts_digit        
        
    def test_calculate_account_bb_invalid(self):
        bank = BANCO_DO_BRASIL['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_bb()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])
      
        assert digits_calculated != accounts_digit
        
    def test_calculate_account_bradesco_valid(self):
        bank = BRADESCO['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_bradesco()
            
            digits_calculated.append(calculate_account)
            if bank[i]['account_digit'] == '0' or bank[i]['account_digit'] == 'P':
                bank[i]['account_digit'] = calculate_account
                
            accounts_digit.append(bank[i]['account_digit'])
    
        assert digits_calculated == accounts_digit  
        
    def test_calculate_account_bradesco_invalid(self):
        bank = BRADESCO['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_bradesco()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])
    
        assert digits_calculated != accounts_digit    
        
    def test_calculate_account_itau_valid(self):
        bank = ITAU['valid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_itau()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        print(digits_calculated)
        print(accounts_digit)
        assert digits_calculated == accounts_digit
        
    def test_calculate_account_itau_invalid(self):
        bank = ITAU['invalid_combinations']
        digits_calculated = []
        accounts_digit = []
        for i in range(len(bank)):
            calculate_account = CalculateAccount(
                agency=bank[i]['branch'],
                account=bank[i]['account']
                
            ).calculate_account_itau()
            
            digits_calculated.append(calculate_account)
            accounts_digit.append(bank[i]['account_digit'])

        assert digits_calculated != accounts_digit
    
 
        