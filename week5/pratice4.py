

class Employee:
    name = ''

class Permenaent (Employee) :
    pay = 0
    bouns = 0

    def __init__(self, pay, bouns) :
        self.pay = pay
        self.bouns = bouns
    def getPayment(self) :
        print("급여 : > ",self.pay + self.bouns)

class Temporary(Employee) :
    tiem = 0
    pay = 0

    def __init__(self, time, pay) :
        self.time = time;
        self.pay = pay;

    def getPayment(self) :
        print("급여 : > ",self.time * self.pay)

empList = []
while True :
    type = input("고용형태 선택(정규직<P>, 임시직<T>) : > ")
    name = input("이름 : > ")
    if type == "T" :
        temp = Temporary(int(input("작업시간 : > ")), int(input("시급 : >") ))
        temp.getPayment()
        empList.append(temp)
    else :
        perme = Permenaent(int(input("급여 : > ")), int(input("상여금 : >") ))
        perme.getPayment()
        empList.append(perme)

