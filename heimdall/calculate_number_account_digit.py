class CalculateAccount:
    def __init__(self, config):
        self.account = config.get('account')
        self.agency = config.get('agency')

    def calculate_account_bb(self):
        """
            Calcula o dígito verificador da conta do Banco do Brasil
        """
        numbers = []
        if len(self.account) < 8:
            self.account = '%08d' % int(self.account)
        
        numbers = [number for number in self.account]
        sumSeq = 0

        for i in range(len(numbers)):
            seq = 9 - int(i)
            sumSeq += (int(numbers[i]) * seq)

        return Modules().module_bb(sumSeq)

    def calculate_account_banrisul(self):
        """
            Calcula o dígito verificador da conta do Banrisul
        """
       
        if len(self.account) < 9:
            self.account = '%09d' % int(self.account)
        
        numbers = [number for number in self.account]
        sumSeq = 0

        for i in range(len(numbers)):
            weight = [3, 2, 4, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_eleven(sumSeq)

    def calculate_account_bradesco(self):
        """
            Calcula o dígito verificador da conta do Bradesco
        """
        if len(self.account) < 7:
            self.account = '%07d' % int(self.account)

        numbers = [number for number in self.account]

        sumSeq = 0
        for i in range(len(numbers)):
            weight = [2, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_bradesco_account(sumSeq)

    def calculate_account_itau(self):
        """
            Calcula o dígito verificador da conta do Itau
        """
        numbers = [number for number in self.account]
        sumSeq = 0
        sequence = 0

        for i in range(len(numbers)):
            number = int(numbers[i])
            sequence = number * (2 if i % 2 == 0 else 1)
            sequence = CalculateAccount._adjust_according_length(sequence)
            sumSeq += sequence

        return Modules().module_itau(sumSeq)

    def calculate_account_santander(self):
        """
            Calcula o dígito verificador da conta do banco Santander
        """
        relevant_data = self.agency + '00' + self.account
        pivot = '97310097131973'
        values = [int(x) * int(y) for x, y in zip(relevant_data.zfill(len(pivot)), pivot)]

        result = sum(values)
        result = 10 - (result % 10)

        return '0' if result == 10 else str(result)

    def calculate_account_citibank(self):
        """
            Calcula o dígito verificador da conta do banco Citibank
        """
        if len(self.account) < 10:
            self.account = '%10d' % int(self.account)

        numbers = [number for number in self.account]
        sumSeq = 0
        for i in range(len(numbers)):
            weight = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            number = int(numbers[i])
            sumSeq += (number * weight[i])

        return Modules().module_citibank(sumSeq)

    def calculate_account_caixa(self):
        """
            Calcula o dígito verificador de uma conta da Caixa Econômica Federal
        """
        pivot = '876543298765432'
        relevant_data = self.agency + self.account
        dv = sum([int(x) * int(y) for x, y in zip(relevant_data.zfill(len(pivot)), pivot)])
        dv *= 10
        dv %= 11
        return '0' if dv == 10 else str(dv)

    def calculate_account_nubank(self):
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

        account_with_zero = str(self.account) + '0'

        number = tuple(int(n) for n in reversed(str(account_with_zero)))
        check = 0
        for i, n in enumerate(number):
            check = multiplicacao[check][permuta[i % 8][n]]

        check_digit = multiplicacao[check].index(0)

        return str(check_digit)

    @staticmethod
    def _adjust_according_length(sequence):
        if sequence > 9:
            numbers_sequence = []

            for number in list(str(sequence)):
                numbers_sequence.append(number)
            
            sequence = 0
            
            for i in range(len(numbers_sequence)):
                sequence += int(numbers_sequence[i])
        
        return sequence

class CalculateAgency:
    def __init__(self, agency):
        self.agency = agency

    def calculate_agency_bb(self):
        """
            Calcula número da agência do Banco do Brasil
        """
        sumSeq = CalculateAgency.calculate_agency_generic(self.agency)
        return Modules().module_bb(sumSeq)

    def calculate_agency_bradesco(self):
        """
          Calcula número da agência do Bradesco
        """
        sumSeq = CalculateAgency.calculate_agency_generic( self.agency)
        return Modules().module_bradesco_agency(sumSeq)

    @staticmethod
    def calculate_agency_generic(agency):
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
    def module_bradesco_agency(sumSeq):
        module = 11 - (sumSeq % 11)
        if module == 10:
            return 'P'

        if module == 11:
            return '0'

        return str(int(module))

    @staticmethod
    def module_citibank(sumSeq):
        module = sumSeq % 11
        if module == 0:
            return '0'

        return str(int(11 - module))

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
