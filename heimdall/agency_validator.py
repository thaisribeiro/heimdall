import re
from heimdall.generic_validators import GenericValidators
from heimdall.calculate_number_account_digit import CalculateAccount, CalculateAgency
from heimdall.common_validate import CommonValidate
from heimdall.base_validate_error import (InvalidAgencyNumber, InvalidDigitAgencyNumber,InvalidAccountNumber, InvalidDigitAccountNumber)

class AgencyValidator(CommonValidate):
    def __init__(self, config):
        self.bank_code = config.get('bank_code')
        self.agency = config.get('agency')

        if len(self.agency) > 4:
            agency = re.sub('[^A-Za-z0-9]+', '', self.agency)
            self.agency = agency[0:4]
            self.digit_agency = agency[4:len(agency)]
        
        if config.get('digit_agency'):
            self.digit_agency = config.get('digit_agency')

    def start(self):
        try:
            switcher = {
                '001': AgencyValidator.valid_agency_bb,
                '237': AgencyValidator.valid_agency_bradesco,
                '341': AgencyValidator.valid_agency_itau,
                '033': AgencyValidator.valid_agency_santander,
                '745': AgencyValidator.valid_agency_citibank,
                '041': AgencyValidator.valid_agency_banrisul,
                '104': AgencyValidator.valid_agency_caixa,
                '260': AgencyValidator.valid_agency_nubank
            }

            result = switcher.get(self.bank_code)()

            if not result:
                return self.valid_agency_generic()

            return result
        except Exception:
            return False

    def valid_agency_generic(self):
        """
        """
        result = GenericValidators.agency_is_valid(self.agency)
        if self.digit_agency:
            result = GenericValidators.agency_digit_is_valid(self.digit_agency)

        return result

    def valid_agency_bb(self):
        """
           Valida a agência e o dígito verificador do banco do Brasil
           Tamanho da Agência - 4 Dígitos + 1 DV
        """
        agency_is_valid = super().agency_is_valid(self.agency)
    
        if not agency_is_valid:
            raise InvalidAgencyNumber()

        digit_agency_is_valid = super().agency_digit_is_valid(self.digit_agency)

        if not digit_agency_is_valid or len(self.digit_agency) != 1:
            raise InvalidDigitAgencyNumber()

        check_number_calculated_digit = CalculateAgency(self.agency).calculate_agency_bb()

        if not check_number_calculated_digit:
            raise InvalidAgencyNumber()

        return check_number_calculated_digit == self.digit_agency.upper()

    def valid_agency_banrisul(self):
        """
          Valida a agência e dígito verificador do banco Banrisul
          Tamanho da Agência - 4 Dígitos
        """
        result = super().agency_is_valid(self.agency)
        if result == False:
            raise InvalidAgencyNumber()
        
        return True

    def valid_agency_bradesco(self):
        """
            Valida a agência e o dígito verificador do banco Bradesco
            Tamanho da Agência - 4 Dígitos + 2 DV
        """
        result = super().agency_is_valid(self.agency)
        if result == False:
            raise InvalidAgencyNumber()

        result = super.agency_digit_is_valid(self.digit_agency)

        if result == False:
            raise InvalidDigitAgencyNumber()


        check_number_calculated_agency = CalculateAgency(self.agency).calculate_agency_bradesco()

        if not check_number_calculated_agency:
            raise InvalidAgencyNumber()
        
        check_number_informed_digit = self.digit_agency.upper()

        if check_number_informed_digit == '0':
            return check_number_calculated_agency == check_number_informed_digit or check_number_calculated_agency == 'P'
        
        return check_number_calculated_agency == check_number_informed_digit

    def valid_agency_citibank(self):
        """
          Valida a agência do banco Citibank
          Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result = super().agency_is_valid(self.agency)

        if result == False:
            raise InvalidAgencyNumber()
        
        return True

    def valid_agency_itau(self):
        """
          Valida a agência do banco Itaú
          Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result = super().agency_is_valid(self.agency)
        if result == False:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_santander(self):
        """
           Valida a agência do banco Santander
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result = super().agency_is_valid(self.agency)

        if result == False:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_caixa(self):
        """
           Valida a agência do banco Caixa Econômica Federal
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result = super().agency_is_valid(self.agency)

        if result == False:
            raise InvalidAgencyNumber()

        return True

    def valid_agency_nubank(self):
        """
           Valida a agência do banco Nu Pagamentos (Nubank)
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        result = super().agency_is_valid(self.agency)

        if result == False:
            raise InvalidAgencyNumber()
        return True

