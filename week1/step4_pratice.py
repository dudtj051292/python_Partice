import math

try:
# q1
    su = 5
    dan = 800
    print('su주소 : %d' %(id(su)))
    print('su주소 : {0}'.format(id(su)))
    print(f'금액 {su*dan}')

# q2
    class equation :
        def __init__(self):
            pass
        def calculate(x ):
            return  2.5 * math.pow(x, 2)+3.3*x+6
            # print(f'2차 방정식 결과 = [{2.5 * math.pow(x, 2)+3.3*x+6}]')
    try :
        # print(equation.calculate(int(input("숫자를 입력하세요 : "))))
        print(f"2차방정식 결과 : [{equation.calculate(int(input('숫자를 입력하세요 : ')))}]")
    except TypeError as ex :
        print('잘못된 타입입니다.\n',ex)
    except ValueError as ex:
        print('숫자만 입력해주세요.\n',ex)

#q3
    try :
        a = int(input('지방의 그램을 입력해주세요 : '))
        b= int(input('탄수화물의 그램을 입력해주세요 : '))
        c = int(input('단백질의 그램을 입력해주세요 : '))
        print(f'총칼로리 { format(a*9 + (b+c)*4, "0,d") } kcal'  )
    except TypeError as ex:
        print('잘못된 타입입니다.\n', ex)
    except ValueError as ex:
        print('숫자만 입력해주세요.\n', ex)

#q4
    val1 , val2 , val3 = input("첫번째 단어 : "),input("두번째 단어 : " ),input("세번째 단어: ")
    print("약자 : {0}" .format(val1[0]+val2[0]+val3[0]))
except KeyboardInterrupt as e :
    print(e)