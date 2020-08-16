import itertools as it


class CalcRank:
    LIST_RANK = [
        'Units_rank', 'Rank_of_tens', 'Rank_of_the_hundreds', 'Thousands_rank',
        'Discharge_tens_of_thousands', 'Discharge_of_hundreds_of_thousands',
        'Discharge_of_millions'
    ]

    def __init__(self, x, y, move):
        self.x = x
        self.y = y
        self.move = move
        self.result = []
        self.pull = 0

    def trans(self):
        self.x = [i for i in self.x]
        self.y = [i for i in self.y]
        self.length()
        self.x.reverse()
        self.y.reverse()

    def length(self):
        if len(self.x) > len(self.y):
            while len(self.x) != len(self.y):
                self.y.insert(0, 0)
        elif len(self.y) > len(self.x):
            while len(self.x) != len(self.y):
                self.x.insert(0, 0)

    def operation_add(self):
        self.trans()
        for i in range(len(self.x)):
            print(f'{CalcRank.LIST_RANK[i].replace("_", " ")}:\n'
                  f'Operation "{self.move}" with {self.x[i]} and {self.y[i]}')
            a = int(self.x[i]) + int(self.y[i]) + self.pull
            if a >= 10:
                print(f'As sum {self.x[i]} and {self.y[i]} equals {a},\n'
                      f'We remember 1 to next rank')
                self.pull = 1
                self.result.append(str(a)[1])
            else:
                print(f'As sum {self.x[i]} and {self.y[i]} equals {a},\n'
                      f'We dont remember nothing')
                self.pull = 0
                self.result.append(str(a))
        if self.pull == 1:
            self.result.append(str(self.pull))
            self.pull = 0

    def operation_sub(self):
        self.trans()
        for i in range(len(self.x)):
            print(f'{CalcRank.LIST_RANK[i].replace("_", " ")}:\n'
                  f'Operation "{self.move}" with {self.x[i]} and {self.y[i]}')
            a = int(self.x[i]) - int(self.y[i]) + self.pull
            if a < 0:
                print(f'As difference {self.x[i]} and {self.y[i]} equals {a},\n'
                      f'Subtract 1 from the most significant bit')
                self.pull = 10
                a = int(self.x[i]) - int(self.y[i]) + self.pull
                self.result.append(str(a))
                self.pull = -1
            else:
                print(f'As difference {self.x[i]} and {self.y[i]} equals {a},\n'
                      f'Subtract nothing')
                self.pull = 0
                self.result.append(str(a))

    def display(self):
        print('\nResult')
        self.result.reverse()
        self.result = list(it.dropwhile(lambda x: x == 0, [int(i) for i in self.result]))
        if not self.result:
            return 0
        else:
            return "".join([str(i) for i in self.result])


if __name__ == '__main__':
    x: str = str(input('Enter first number:\n'))
    y: str = str(input('Enter second number:\n'))
    move: str = str(input('Enter operation (-\\+):\n'))
    calc = CalcRank(x, y, move)
    if move == '+':
        calc.operation_add()
    elif move == '-':
        calc.operation_sub()
    result = calc.display()
    print(result)