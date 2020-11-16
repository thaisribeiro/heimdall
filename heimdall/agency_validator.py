class AgencyValidator():
    def __init__(self, config):
        self.config = config
    
    def start(self):
        # validação de agencia com digito
        
        switcher = {
            '001': AgencyValidator.valid_agency_bb,
            '237': AgencyValidator.valid_agency_bradesco,
            '341': AgencyValidator.valid_agency_itau,
            '033': AgencyValidator.valid_agency_santander,
            '745': AgencyValidator.valid_agency_citibank,
            '399': AgencyValidator.valid_agency_hsbc,
            '041': AgencyValidator.valid_agency_banrisul
        }

        params = switcher[self.config.get('bank_code')](self.config)

    def valid_agency_bb(self, config):
        return {}

    def valid_agency_itau(self, config):
        return {}

    def valid_agency_bradesco(self, config):
        return {}

    @staticmethod
    def valid_agency_santander(self, config):
        return {}
    
    @staticmethod
    def valid_agency_banrisul(self, config):
        return {}
    
    
    def valid_agency_santander(self, config):
        return {}
    
    def valid_agency_citibank(self, configf):
        return {}

    def valid_agency_hsbc(self, AgencyValidator):
        return {}