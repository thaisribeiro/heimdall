class CalculateAccountCheckDigit():
    def __init__(self, account):
        # account é a conta e o digito
        self.account = account
    
    def calculate_check_digit_account_bb(self):
        """
            Calcula o dígito verificador da conta do Banco do Brasil
        """
        numbers = []
        left_zeros = 8 - len(self.account)

        for x in range(left_zeros):
            numbers.append('0')

        for number in self.account:
            numbers.append(number)

        sumSeq = 0
       
        for i in range(len(numbers)):
            seq = 9 - i
            sumSeq += (int(numbers[i]) * seq)

        return Modules().module_bb(sumSeq)

    def calculate_check_digit_account_banrisul(self):
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

    def calculate_check_digit_account_santander(self):
        """
            Calcula o dígito verificador do banco Santander
        """
        pivot = '97310097131973'
        values = [int(x) * int(y) for x, y in zip(self.account.zfill(len(pivot)), pivot)]

        result = sum(values)
        result = 10 - (result % 10)

        return '0' if result == 10 else result

    def calculate_check_digit_account_citibank(self):
        """
            Calcula o dígito verificador do banco Citibank
        """
        numbers = [0,0,0]

        for number in self.account:
            numbers.append(numbers)

        sumSeq = 0
        for i in range(len(numbers)):
            weight = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_citibank_account(sumSeq)

    
    def calculate_check_digit_account_bradesco(self):
        """
            Calcula numero da conta do Bradesco
        """
        numbers = []
        left_zeros = 7 - len(self.account)

        for x in range(left_zeros):
            numbers.append('0')

        for number in self.account:
            numbers.append(number)
        
        sumSeq = 0
        for i in range(len(numbers)):
            weight = [2,7,6,5,4,3,2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_bradesco_account(sumSeq)
    
    def calculate_check_digit_account_itau(self):
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

    def calculate_check_digit_account_caixa(self):
        """
            Calcula o dígito verificador de uma conta da Caixa Econômica Federal
        """
        account_relevant_data = self.agency + self.account
        pivot = '876543298765432'
        dv = sum([int(x) * int(y) for x, y in zip(account_relevant_data.zfill(len(pivot)), pivot)])
        dv *= 10
        dv %= 11
        return '0' if dv == 10 else dv

    def calculate_check_digit_account_nubank(self):
        """
            Calcula o dígito verificador de uma conta Nu Pagamentos (Nubank)
        """
        multiplicacao = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
                         [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
                         [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
                         [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
                         [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
                         [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
                         [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
                         [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
                         [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]

        permuta = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                   [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
                   [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
                   [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
                   [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
                   [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
                   [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
                   [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

        inversao = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]

        number = tuple(int(n) for n in reversed(str(self.account)))
        i = len(number)
        j = 0
        x = 0

        while i > 0:
            i -= 1
            j += 1
            x = multiplicacao[x][permuta[(j % 8)][int(number[i])]]

        return inversao[x]

class CalculateAgencyCheckDigit():
    def __init__(self, agency):
        self.agency = agency

    def calculate_check_digit_agency_bb(self):
        """
            Calcula número da agência do Banco do Brasil
        """
        sumSeq = self.calculate_check_digit_agency_generic(self.agency)
        return Modules().module_bb(sumSeq)
    
    def calculate_check_digit_agency_bradesco(self):
        """
          Calcula número da agência do Bradesco
        """
        sumSeq = CalculateAgencyCheckDigit.calculate_check_digit_agency_generic( self.agency)
        return Modules().module_bradesco_agency(sumSeq)

    def calculate_check_digit_agency_banrisul(self):
        """
          Calcula o dígito verificador da agência do banco Banrisul
        """
        sumSeq = CalculateAgencyCheckDigit.calculate_check_digit_agency_generic(self.agency)
        return Modules().module_banrisul_agency(sumSeq)

    @staticmethod
    def calculate_check_digit_agency_generic(agency):
        numbers = []
        for number in agency:
            numbers.append(number)
        
        sumSeq = 0
        
        for i in range(len(numbers)):
            seq = 5 - i
            sumSeq += (float(numbers[i]) * seq)

        return sumSeq

class Modules():
    @staticmethod
    def module_bb(sumSeq):
        result = 11 - (sumSeq % 11)
        if result == 10:
            return 'X'
        if result == 11:
            return '0'
        
        return str(int(result))
    
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

        return str(int((11 - module)))

    @staticmethod
    def module_citibank_account(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return '0'

        return (11 - module)
    
    @staticmethod
    def module_bradesco_agency(sumSeq):
        module = 11 - (sumSeq % 11)
        if module == 10:
            return 'P' 

        if module == 11:
            return '0'

        return str(int(module))

    @staticmethod
    def module_banrisul_agency(sumSeq):

        def sum_digits(value):
            return sum([int(x) for x in str(value)])

        first_digit = 10 - ((sum_digits(int(sumSeq[0]) * 1) +
                             sum_digits(int(sumSeq[1]) * 2) +
                             sum_digits(int(sumSeq[2]) * 1) +
                             sum_digits(int(sumSeq[3]) * 2)) % 10)

        if first_digit == 10:
            first_digit = 0

        second_digit = 11 - ((int(sumSeq[0]) * 6 +
                              int(sumSeq[1]) * 5 +
                              int(sumSeq[2]) * 4 +
                              int(sumSeq[3]) * 3 +
                              first_digit * 2) % 11)

        if second_digit == 11:
            second_digit = 0
        elif second_digit == 10:
            first_digit = (first_digit + 1) % 10
            second_digit = 11 - ((int(sumSeq[0]) * 6 +
                                  int(sumSeq[1]) * 5 +
                                  int(sumSeq[2]) * 4 +
                                  int(sumSeq[3]) * 3 +
                                  first_digit * 2) % 11)

        return str(first_digit) + str(second_digit)

    @staticmethod
    def module_itau(sumSeq):
        module = sumSeq % 10
        if module == 0:
            return '0'
        
        return str((10 - module))