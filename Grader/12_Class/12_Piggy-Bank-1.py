class piggybank:
    def __init__(self):
        self.one = 0
        self.two = 0
        self.five = 0
        self.ten = 0
    def add1(self, n):
        self.one += n
    def add2(self, n):
        self.two += n
    def add5(self, n):
        self.five += n
    def add10(self, n):
        self.ten += n
    def __int__(self):
        return (self.one)+(self.two*2)+(self.five*5)+(self.ten*10)
    def __lt__(self, rhs):
        return self.__int__() < rhs.__int__()
    def __str__(self):
        return '{1:'+str(self.one)+', 2:'+str(self.two)+', 5:'+str(self.five)+', 10:'+str(self.ten)+'}'

cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)