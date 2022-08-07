import  statistics
from statistics import variance, stdev
import builtins
import re

dataset = list(range(1,6))
print(dataset)
print('평균 = {0}'.format(statistics.mean(dataset)))
print('중위수 = {0}'.format(statistics.median(dataset)))

print('표본분산 = {0}'.format(statistics.variance(dataset)))

print('표본 표준편차 = {0}'.format(statistics.stdev(dataset)))



print(dir(builtins))

print(list(zip(['가','나','다'], [2,3,5,8])))


def clear_text() :
    text = input("게시판에 담길 글을 입력하세요 ")
    # 욕변경
    slang = ["ㅅㅂ", "ㅈㄴ"]
    for str in slang :
        if str in text :
            text = text.replace(str,"***")
    # !@#$%^&* 0~9 -> ''
    temp_text = []
    for idx in range(len(text)) :
        i = ord(list(text)[idx])
        if(  (65 <= i and i <=90) or (87 <= i and i <=122)  ) :
            temp_text.append(list(text)[idx])
        else :
            temp = list(text)[idx] = ""
            temp_text.append(temp)
        # print(ord(list(text)[str]) , end=" " )
    print("temp_text : {0}".format(temp_text))
    text = ''.join(temp_text)
    # 영문 -> 대문자
    text = text.upper()
    # 공백제거
    text = text.strip();

    return text

print("결과 : {0} ".format(clear_text()))



