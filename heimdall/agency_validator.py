import re
from generic_validators import GenericValidators
from calculate_number_account_agency import CalculateNumberAgency
from common_validate import CommonValidate
from base_validate_error import InvalidAgencyNumber, InvalidDigitAgencyNumber,InvalidAccountNumber, InvalidDigitAccountNumber, InvalidCodeBankP 

class AgencyValidator(CommonValidate):
    def __init__(self, config):
        self.config = config

    def start(self):
        try:
            # validação de agencia com digito
            bank_code = self.config.get('bank_code')
            agency_code = self.config.get('agency')

            if len(agency_code) > 4:
                agency = re.sub('[^A-Za-z0-9]+', '', agency_code)
                self.config.update({
                    'agency': agency[0:4],
                    'digit_agency': agency[4:len(agency)]
                })

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

            result = switcher.get(bank_code)()

            if not result:
                return self.valid_agency_generic()

            return result
        except Exception:
            print('Erro')

    def valid_agency_generic(self):
        agency = self.config.get('agency')
        digit_agency = self.config.get('digit_agency')

        result = GenericValidators.agency_is_valid(agency)
        if digit_agency:
            result = GenericValidators.agency_digit_is_valid(digit_agency)

        return result

    def valid_agency_bb(self):
        """
           Valida a agência e o dígito verificador do banco do Brasil
           Tamanho da Agência - 4 Dígitos + 1 DV
        """
        agency = self.config('agency')
        digit_agency = self.config.get('digit_agency')

        result = super().agency_is_valid(agency)
        if result == False:
            raise InvalidAgencyNumber(agency)

        result = GenericValidators.agency_digit_is_valid(agency)
        if result == False:
            raise InvalidDigitAgencyNumber(agency)

        calculated_agency_digit = CalculateNumberAgency.calculate_number_agency_bb(digit_agency)

        if not calculated_agency_digit:
            raise InvalidDigitAgencyNumber()

        return True

    def valid_agency_itau(self):
        """
          Valida a agência do banco Itaú
          Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        agency = self.config('agency')
        result = super().agency_is_valid(agency)
        
        if result == False:
            raise InvalidAgencyNumber(agency)
        return True

    def valid_agency_bradesco(self):
        """
            Valida a agência e o dígito verificador do banco Bradesco
            Tamanho da Agência - 4 Dígitos + 2 DV
        """
        agency = self.config('agency')
        digit_agency = self.config.get('digit_agency')

        result = CommonValidate.agency_is_valid(agency)
        if result == False:
            raise InvalidAgencyNumber(agency)


        result = CommonValidate.agency_digit_is_valid(agency)
        if result == False:
            raise InvalidDigitAgencyNumber(agency)

        calculated_agency_digit = CalculateNumberAgency.calculate_number_agency_bradesco(digit_agency)

        if not calculated_agency_digit:
            raise InvalidDigitAgencyNumber()

        return True

    def valid_agency_santander(self):
        """
           Valida a agência do banco Santander
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        agency = self.config('agency')
        result = super().agency_is_valid(agency)

        if result == False:
            raise InvalidAgencyNumber(agency)
        return True

    def valid_agency_banrisul(self):
        """
          Valida a agência e dígito verificador do banco Citibank
          Tamanho da Agência - 4 Dígitos + 2 DV
        """
        agency = self.config('agency')
        digit_agency = self.config.get('digit_agency')

        result = CommonValidate.agency_is_valid(agency)
        if result == False:
            raise InvalidAgencyNumber(agency)

        result = CommonValidate.agency_digit_is_valid(agency)
        if result == False:
            raise InvalidDigitAgencyNumber(agency)

        calculated_agency_digit = CalculateNumberAgency.calculate_number_agency_banrisul(digit_agency)

        if not calculated_agency_digit:
            raise InvalidDigitAgencyNumber()

        return True

    def valid_agency_citibank(self):
        """
          Valida a agência do banco Citibank
          Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        agency = self.config('agency')
        result = super().agency_is_valid(agency)

        if result == False:
            raise InvalidAgencyNumber(agency)
        return True

    def valid_agency_caixa(self):
        """
           Valida a agência do banco Caixa Econômica Federal
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        agency = self.config('agency')
        result = super().agency_is_valid(agency)

        if result == False:
            raise InvalidAgencyNumber(agency)
        return True

    def valid_agency_nubank(self):
        """
           Valida a agência do banco Nu Pagamentos (Nubank)
           Tamanho da Agência - 4 Dígitos - Não tem dígito verificador
        """
        agency = self.config('agency')
        result = super().agency_is_valid(agency)

        if result == False:
            raise InvalidAgencyNumber(agency)
        return True

