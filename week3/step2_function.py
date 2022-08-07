import random


def add(a,b) :
    print("{0} + {1} = {2}".format(a,b,a+b))
    return a+b

def minus(a,b) :
    print("{0} - {1} = {2}".format(a,b,a-b))
    return a-b

def multi(a,b) :
    print("{0} * {1} = {2}".format(a,b,a*b))
    return a*b

def divide(a,b) :
    print("{0} / {1} = {2}".format(a,b,a/b))
    return a/b

print(minus(add(10,20),10) )
print(divide(10,20))
print(multi(5,1.578))


while (False) :
    a = int(input('연산할 첫번째 수를 입력하세요'))
    b = int(input('연산할 두번째 수를 입력하세요'))
    oper = input('진행할 연산자를 입력해주세요 ( +, - , * , /) ')
    if oper == "+" :
        add(a,b)
    elif oper == "-" :
        minus(a,b)
    elif oper == "*":
        multi(a, b)
    elif oper == "/" :
        divide(a,b)
    elif oper == "exit" :
        break;
    else :
        print("없는 연산자입니다.")


subject = {"python":100 , "java": 90 , "html":88}

def getSubPoint() :
    sub = input("확인할 과목을 입력하세요 : ")
    if sub in  subject.keys() :
        print("{1}과목의 점수는 {0}점입니다.".format(subject[sub],sub))
    else :
        print("확인 할 수 없는 과목입니다.")

# getSubPoint();


def lotto() :
    myLotto = set()
    i = 0
    while(True) :
        i+=1
        print("{0}번째..".format(i) )
        num = random.randint(1,46)
        myLotto.add(num)
        if(len(myLotto) ==6) :
            break
    return myLotto

print(lotto())