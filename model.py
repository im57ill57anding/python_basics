import math


class Computation:
    def getFactorial(self, number: int):
        answer: int = 0

        for i in range(1, number + 1):
            answer *= i

        return answer

    def getSum(self, number: int):
        answer: int = 0

        for i in range(1, number + 1):
            answer += i

        return answer

    def checkPrime(self, number: int):
        root = int(math.sqrt(number))

        for i in range(2, root + 1):
            if number % i == 0:
                return False

        return True

    def getPrimes(self, left: int, right: int):
        answer: list = []

        for i in range(left, right+1):
            if self.checkPrime(i):
                answer.append(i)

        return answer

    def getMultiplicationTable(self, number: int):
        answer: list = []

        for i in range(0, 10):
            answer.append(f'{i} * {number} = {i * number}')

        return answer

    def getAllMultiplicationTables(self, number: int):
        answer: list = []

        for i in range(0, number+1):
            answer.append(self.getMultiplicationTable(i))

        return answer

    def getListOfDivisors(self, number: int):
        answer: list = []
        root = int(math.sqrt(number))

        for i in range(2, root + 1):
            if number % i == 0:
                answer.append(i)

        return answer

    def prime_divisors(self, number: int):
        answer: list = []
        root = int(math.sqrt(number))

        for i in range(2, root + 1):
            if number % i == 0 and self.checkPrime(i):
                answer.append(i)

        return answer

    def test(self):
        print(f'getFactorial: {self.getFactorial(5)}')
        print(f'getSum: {self.getSum(10)}')
        print(f'checkPrime: {self.checkPrime(19)}')
        print(f'getPrimes: {self.getPrimes(3, 29)}')
        print(f'getMultiplicationTable: {self.getMultiplicationTable(7)}')
        print(f'getAllMultiplicationTables: {self.getAllMultiplicationTables(3)}')
        print(f'prime_divisors: {self.prime_divisors(27)}')
