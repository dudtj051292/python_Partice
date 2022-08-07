import datetime
import random

stringtime = datetime.datetime.now()
oddList = []
evenList = []
for i in range (1, 100) :
    if(i %2 ==0):
        evenList.append(i)
    else :
        oddList.append(i)

print('짝수 : ', evenList)
print('홀수 : ', oddList)

# 소수찾기
def divideNumber(number) :
    cnt = 0
    for j in range (1,number) :
        if ( number % j ==0 ) :
            cnt +=1
            if(cnt>2) :
                return False
    if(cnt ==2) :
        return True

primenumbers = []
for i in range (1, 10000) :
    if(divideNumber(i)) :
        primenumbers.append(i)

print('100까지 숫자중 소수 : ' ,primenumbers)
print(datetime.datetime.now() - stringtime )

today = datetime.datetime.now()
month = 3

if month in range (3 ,6) :
    print('봄', end='? ')
elif month in range (6 ,9) :
    print('여름', end='! ')
elif month in range (9 ,12) :
    print('가을', end='@ ')
else  :
    print('겨울')

