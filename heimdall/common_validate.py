import re

class CommonValidate:
    
    @staticmethod
    def pattern_agency_validate(agency_number):
        if len(agency_number) > 4:
            agency_number = agency_number[0:4]
            digit_agency =  agency_number[3:len(agency_number)]
            CommonValidate.pattern_digit_agency_validate(digit_agency)
        
        regex =  re.compile('(?!0000)([0-9]{4})', re.I)
        match = bool(regex.match(agency_number))
        
        if match == False:
            raise ValueError('A agência deve conter 4 números. Complete com zeros a esquerda se necessário')
        
        return True

    @staticmethod
    def pattern_digit_agency_validate(digit_agency=None):
        regex =  re.compile('[a-zA-Z0-9]{0,1}', re.I)
        match = bool(regex.match(digit_agency))

        if match == False:
            raise ValueError('Digito da agência inválido')
        
        return True