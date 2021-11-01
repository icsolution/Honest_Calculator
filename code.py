class Calculator:
    def __init__(self):
        self.equation = self.result = self.memory = '0'

    def run(self):
        self.get_equation()
        self.calculate()
        print(self.result)
        self.save()

    def get_equation(self):
        print('Enter an equation')
        self.equation = input().split()
        try:
            for index, choice in enumerate(self.equation):
                if choice == 'M':
                    self.equation[index] = str(self.memory)
            self.check_difficulty()
            float(self.equation[0]) + float(self.equation[2])
            if self.equation[1] not in ['+', '-', '*', '/']:
                print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
                self.get_equation()
            elif self.equation[1] + self.equation[2] == '/0':
                print('Yeah... division by zero. Smart move...')
                self.get_equation()
            else:
                return self.equation
        except ValueError:
            print('Do you even know what numbers are? Stay focused!')
            self.get_equation()

    def calculate(self):
        if self.equation[1] == '+':
            self.result = float(self.equation[0]) + float(self.equation[2])
        elif self.equation[1] == '-':
            self.result = float(self.equation[0]) - float(self.equation[2])
        elif self.equation[1] == '*':
            self.result = float(self.equation[0]) * float(self.equation[2])
        elif self.equation[1] == '/':
            self.result = float(self.equation[0]) / float(self.equation[2])
        return self.result

    def save(self):
        answer = input('Do you want to store the result? (y / n):\n')
        chances = ['Are you sure? It is only one digit! (y / n)\n',
                   "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
                   "Last chance! Do you really want to embarrass yourself? (y / n)\n"]
        if answer == 'y':
            if self.is_one_digit(self.result):
                for chance in chances:
                    answer = input(chance)
                    if answer == 'y':
                        if chance != chances[2]:
                            pass
                        else:
                            self.memory = self.result if int(float(self.result)) != float(self.result) else int(self.result)
                            break
                    elif answer == 'n':
                        break
            else:
                self.memory = self.result if int(float(self.result)) != float(self.result) else int(self.result)
        answer = input('Do you want to continue calculations? (y / n):\n')
        if answer == 'y':
            self.run()
        else:
            exit()

    def check_difficulty(self):
        number1, operator, number2 = self.equation
        message = ''
        if self.is_one_digit(number1) and self.is_one_digit(number2):
            message += ' ... lazy'
        if operator == '*' and '1' in self.equation:
            message += ' ... very lazy'
        if operator in '*+-' and '0' in self.equation:
            message += ' ... very, very lazy'
        if message:
            print(f'You are{message}')

    @staticmethod
    def is_one_digit(number):
        if int(float(number)) == float(number) and -10 < int(float(number)) < 10:
            return True
        else:
            return False


if __name__ == '__main__':
    smart_calc = Calculator()
    smart_calc.run()
