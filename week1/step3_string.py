
'''
문자열 특징
 - 문자들의 집합 [] : 리스트
 - 순서(index)를 갖는다
 - 문자열 처리 함수 제공
'''

oneLine = 'this is one line String'
print(oneLine)

multiList = '''Hi, My name is Youngsuh
glad to meet you
'''

multiLine2 = '    this is\nmulti line\nstring    '
print(multiLine2)

print('find multi : ' ,multiLine2[multiLine2.find('m')-1 : multiLine2.find('m') +len('multi') ])
print("-".join(multiLine2.strip()).split('-'))
print(multiLine2.strip())
print(multiLine2.replace('multi', 'single').strip().replace('\n', ''))


val1 , val2 , val3 = input("첫번째 단어 : "),input("두번째 단어 : " ),input("세번째 단어: ")
print("약자 : {0}" .format(val1[0]+val2[0]+val3[0]))
print(val1[0])