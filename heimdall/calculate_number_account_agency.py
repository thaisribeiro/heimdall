class CalculateNumberAccount():
    def __init__(self, account):
        # account é a conta e o digito
        self.account = account
    
    def caculate_number_account_bb(self):
        """
            Calcula numero da conta do Banco do Brasil
        """
        numbers = []
        for number in self.account:
            numbers.append(number)

        sumSeq = 0
       
        for i in range(len(numbers)):
            seq = 9 - i
            sumSeq += (int(numbers[i]) * seq)

        return Modules().module_bb(sumSeq)

    def calculate_number_account_banrisul(self):
        """
            Calcula numero da conta do Banrisul
        """
        numbers = []
        for number in self.account:
            numbers.append(number)

        sumSeq = 0

        for i in range(len(numbers)): 
            weight = [3,2,4,7,6,5,4,3,2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_eleven(sumSeq)
    
    def calculate_number_account_bradesco(self):
        """
            Calcula numero da conta do Bradesco
        """
        numbers = []
        for number in self.account:
            numbers.append(numbers)
        
        sumSeq = 0
        for i in range(len(numbers)):
            weight = [2,7,6,5,4,3,2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_bradesco_account(sumSeq)
    
    def calculate_number_itau(self):
        """
            Calcula o número da conta do Itau
        """
        numbers = []
        for number in self.account:
            numbers.append(number)

        sumSeq = 0
        sequence = 0
        for i in range(len(numbers)):
            number = int(numbers[i])
            sequence = number * (2 if i % 2 == 0 else 1)
            
            if sequence > 9:
                numbers_sequence = []

                for n in sequence:
                    numbers_sequence.append(n)

                sequence = 0

                for idx in range(len(numbers_sequence)):
                    sequence += int(numbers_sequence[idx])

            sumSeq += sequence
            return Modules().module_itau(sumSeq)
    

class CalculateNumberAgency():
    def __init__(self, agency):
        self.agency = agency

    def calculate_number_agency_bb(self):
        """
            Calcula número da agência do Banco do Brasil
        """
        sumSeq = self.calculate_number_agency_generic()    
        return Modules().module_bb(sumSeq)
    
    def calculate_number_agency_bradesco(self):
        """
          Calcula número da agência do Bradesco
        """
        sumSeq = self.calculate_number_agency_generic()
        return Modules().module_bradesco_agency(sumSeq)
    
    def calculate_number_agency_generic(self):
        numbers = []
        for number in self.agency:
            numbers.append(number)
        
        sumSeq = 0
        
        for i in range(len(numbers)):
            seq = 5 - i
            sumSeq = int(numbers[i] * seq)

        return sumSeq

class Modules():
    @staticmethod
    def module_bb(sumSeq):
        result = 11 - (sumSeq % 11)
        if result == 10:
            return 'X'
        if result == 11:
            return '0'
        
        return str(result)
    
    @staticmethod
    def module_eleven(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return 0
        
        if module == 1:
             return 6

        return 11 - module
        
    @staticmethod
    def module_bradesco_account(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return '0' 

        if module == 1:
            return 'P'

        return (11 - module)
    
    @staticmethod
    def module_bradesco_agency(sumSeq):
        module = 11 - (sumSeq % 11)
        if module == 10:
            return 'P' 

        if module == 11:
            return '0'

        return str(module)

    @staticmethod
    def module_itau(sumSeq):
        module = sumSeq % 10
        if module == 0:
            return '0'
        
        return str((10 - module))