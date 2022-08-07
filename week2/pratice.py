
#q1 A
import random


def baggage(x) :
    if(x<10) :
        return '수수료는 없습니다.'
    else :
        return '수수료는 10,000원 입니다.'

#print(baggage(int(input('짐의 무게를 입력하세요 : '))))

#q1 B
def baggage2(x) :
    default = 10000
    if(x<10) :
        return '수수료는 없습니다.'
    else :
        return f'수수료는 {default * (x//10) }원 입니다.'

# print(baggage2(int(input('짐의 무게를 입력하세요 : '))))


#q2
# print('>> 숫자맞추기 게임 << ')
# x = random.randint(1,10)
# my = 0
# while x != my :
#     my = int(input('예상 숫자를 입력하세요! : '))
#     if(my > x) :
#         print('Down!')
#     elif(my<x ):
#         print('UP!')
#     else:
#         print('정답입니다!')


#q3
sum = 0
lst = []
for i in range(1, 100 ) :
    if(i%3 == 0 and  not(i%2 ==0) ) :
        lst.append(i)
        sum +=i
print('수열 : {0}'.format(lst))
print('누적합 : %d' %sum)

#q4
multiline = '''안녕하세요. 페이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다'''
print(multiline.split())
print('단어 개수 : ', len(multiline.split()))