import math

n1 = 10
n2 = 20

result = False

result = n1 ==n2
print(result)

result = n1 !=n2
print(result)

## 연산자 관련 ..

v1 , v2 = 10,20
print(v1, v2)

v2 , v1 = v1 , v2
print(v1, v2)

#패킹할당 함더 조사해보자
lst = [1,2,3,4,5]
v1 , v2 , *v3 = lst
print(v1,v2,v3)

# try :int
#     number = int(input("input number : "))
#     number2 = int(input("input number2 : "))
#     print(number, number2)
#     result = number > number2
#     if (number > number2):
#         print("number1 이[", number - number2, "]만큼 더 큽니다")
#     elif (number == number2):
#         print("두 수는 같습니다.")
#     else:
#         print("number2가 [", number2 - number, "]만큼 더 큽니다")
# except ValueError as ex:
#     print(ex)
# except TypeError as ex :
#     print(ex)

b = 'q'
while(b != 'q'):
    try :
        val1 = int(input("분자를 입력하세요 : "))
        val2 = int(input("분모를 입력하세요 : "))
        print("몫 : [", val1//val2,"]")
        print("나머지 : [", val1%val2,"]")
    except ValueError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    b = input("q키를 누르면 종료됩니다")


#help(내장함수)

print('010','8910','2198', sep='-')

str1 = "파이썬 기능 짱"

print(str1[2])

var1 = [1,2,3,4,5]
print('var1[0] :', var1[0], id(var1[0]))
print('var1[1] :', var1[1], id(var1[1]))
print('var1[2] :', var1[2], id(var1[2]))

# type() dataType 알아보기
print(type(var1))
print(type("var1"))

# format 내장함수
print(format(323.141592, '10.3f'))
print(format(32333, '10d'))
print(format(32113, '10,d'))

# 선언 2번째 방법
num1 , num2 = 10,20
# 선언 3번째 방법
num1 = 10 ; num2 = 20

print('%d + %d = %d' %(num1 ,num2  ,num1+num2))

# print( "이름은 %s 이고 나이는 %d입니다." %(input("이름 : "), int(input("나이 : "))))
print( "이름은 {0} 이고 나이는 {1}입니다." .format('홍길동', 35))

hello = 'HELLO WORLD!'
print(hello[2:4])

print(f"이름은 {'김영서'} 이고 나이는 {'31'}입니다.")


print('Reduce the indexing time and CPU load with pre-built Python packages shared indexes'.find('CPU'))


class equation :
    def __init__(self):
        pass

    def calculate(x ):
        print(f'y = [{2.5 * math.pow(x, 2)+3.3*x+6}]')

try :
    print(equation.calculate(int(input("숫자를 입력하세요 : "))))
except TypeError as ex :
    print(ex)
except ValueError as ex:
    print(ex)