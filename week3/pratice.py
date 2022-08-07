import random

noList = [10,1,5,2]
# 리스트 두배확장
noList *= 2
print(noList)

print(id(noList[0]))

print(id(noList[1]))

print(id(noList[2]))
noList[2] = 4
print(id(noList[2]))
noList[2] = 5
print(id(noList[2]))

# 첫번째 인덱스 값에 *2 하기
noList[0]*2
print((noList))

# 홀수인덱스 요소

for i in noList :
    if noList.index(i) %2 == 1 :
        print("{0}".format(i), end=" ")
print()

for i in noList :
    if i %2 == 1 :
        print("{0}".format(i), end=" ")



# A형 List 크기를 키보드로 입력 받은 후 입력받은 크기만큼 임의 숫자를 list를 생성

#listSize = (int)(input("생성할 리스트 크기? : "))
# 이게되네.. .미쳣나봐..

tempList2 = [random.randint(0,100) for _ in range(10) ]
tempList = set(tempList2)
print(tempList2)
# B형 Guess Number

while(False):
    num = (int)(input("예상수를 입력해주세요 : "))
    if   tempList2.count(num)  > 0:
        print("{0}은 있습니다.".format(num))
        print(tempList2)
        tempList.remove(num)
        print(tempList)
    else :
        print("{0}은 없습니다.".format(num))
        print(tempList)
    if(len(tempList) == 0 ) :
        break

print("모든 수를 맞추셨습니다!!")
print(tempList2)


#4 position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수 출력

# 직위 사장 과장 대리 부장
position = ["과장" , "대리","과장" , "대리","사장", "차장", "차장","부장","부장", "사장", "대리","대리","대리"]
posi_set = { }
for p in position :
    posi_set[p] = posi_set.get(p,0) +1
print(posi_set)


message = ['spam' , 'ham', 'spam', 'ham']
trans_message = [ "1" if msg == "spam" else "0"  for msg in message  ]

print(trans_message)
