'''
Fucntion
 - 특정한 기능을 정의
  - 내장 함수, 사용자 저으이 함수
   1. 내장함수 : built-in or import
   2. 사용자 정의 함수
    def 함수(인수) :


'''
import random

dataset = list(range(1,6));

print(dataset)

# 1) builts in 함수

print('len = {}'.format(len(dataset)))
print('sum =', sum(dataset))
print('max =', max(dataset))
print('min =', min(dataset))


#(2) Import 함수

import statistics

print('평균 =', statistics.mean(dataset))
print('중위수 = ', statistics.median(dataset) )

from statistics import variance, stdev

print('표본 분산 = ', variance(dataset))
print('표본 표준편차 = ', stdev(dataset))


# 2. 사용자 정의 함수
# 인수가 없는 함수

def userFunc1() :
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1()


def userFunc2(x ,y) :
     print('x + y = ',x+y)
     print('funcFucn2')

userFunc2(4,6)



# 3

def userFunc3(x, y) :
    print('userFucn3')
    t = x+y
    d = x/y
    s = x-y
    m = x*y
    return t, d, s,m

tot, div , sum, mul = userFunc3(10,20)

print(tot, sum, div, mul)

i_List = [_*random.randint(0,100) for _ in range(10)]


#함수 매개인자 리스트

def findSosu(x) :
    cnt = 0
    sosu = 0
    for _ in range(2,x) :
        if( x % _ == 0 ) :
            sosu += _
    return sosu


def printList(list) :
    rList = []
    for _ in list :
        rList.append(findSosu(_))
    return rList

print(i_List)
numberList = printList(i_List)


print(dir(list))


# 함수의 가변인수
# 한개 가인수로 여러개 실인수를 받을 수 있는 인수
# 형식 def  함수(*인수)

def userFunc4(name, grade, *subject) :
    print(name)
    print(grade)
    print(subject)

userFunc4("아이유", "1학년", "JAZZ", "R&B", "POP")


from statistics import mean, variance, stdev

def static (type, *data) :
    if type == "avg" :
        return mean(data)
    elif type == "var" :
        return variance(data)
    elif type == "std" :
        return stdev(data)

print(static("avg", 1,2,3,4,5,6))


def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

emp_func('홍길동', 35, addre ='서울시', height =175 , weight =65 , phone = '01089102198')


def coin(n) :
    result = []
    for i in range(n) :
        r = random.randint(0,1)
        if r == 1 :
            result.append(1)
        else :
            result.append(0)
    return result

print(coin(10))

def montaCoin(n) :
    coin_set = coin(15)
    # print('앞면 : {0}회'.format(sum(coin_set)))
    # print("통계 : {0}".format(sum(coin_set)/n))
    # return sum(coin_set)/n

print(montaCoin(30))

def Adder(x,y):
    add = x + y
    return add

print('add = ', Adder(10,20))

print('add = ',(lambda x, y: x+y)(20,30))

