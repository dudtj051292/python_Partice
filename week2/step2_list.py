import random

muhan = "유재석 박명수 정준하 정형돈 노홍철 하하 광희 길"
member_list = [ _ for _ in muhan.split() ]

print(member_list)

print('올해의 mvp 후보 명단입니다 {}'.format(member_list))
choice_member = random.choices(member_list, k=3)
print('올해의 mvp최종 후보 명단입니다.{}'.format(choice_member))
prize_member = random.choices(choice_member)
print('올해의 mvp입니다.{}'.format(prize_member))


a= [1,2,3,4,5]

print(a)
print(type(a))

for _ in range(len(a)) :
    print(a[_:]);


x = list(range(1,11))
print(x)

# 중첩 리스트 객체 생성
b = [10,20, a, 5, True, 'string']
print(b)

aa = [[1,2,3], [4,5,6], [7,8,9]]
print(aa)
print(len(aa))
for _ in range(len(aa)*len(aa)) :
    if _ % len(aa) == 1  :
        # print ("{2}, {0} / {1} ".format(int(_/len(aa)),int(_% len(aa)), _  ))
         print(aa[int(_/len(aa))  ][int(_%len(aa) )], end=' ')


# 4행 5열의 리스트를 만들고 0~3의 배수를 입력하고 출력

beasu = 3 #int(input("n을 입력하세요 : "))

resultList = []
for num in range(0,5) :
    tmplist = [_*beasu +(num * 5 * beasu ) for _ in range(0,5)]
    resultList.append(tmplist)

for i in range(len(resultList)):
    for j in range(len(resultList[0])) :
        print("%3d"%resultList[i][j], end="")
    print()
# print(resultList)

# 0 3 6 9 12
# 15 18 ..
# 0 1 2 3 4
# 0 1 2 3 4 +5
# 0 1 2 3 4 +10

x = list(range(1,11))
print(x)
print(x[:5])
print(x[-5:])

y = [1.5, 2.5]
z = x+y
print (z)

x.extend(y)
print (x)

list1 = [1,2,3,4]
list_reuslt = list1 *2
print (list_reuslt)

buliding = [[7,1,2,3], [5,3,1,5,2], [2,6], [4,4], [1,4,6] ]
summary = 0
for i in range(len(buliding)) :
    for j in range(len(buliding[i])) :
        summary += buliding[i][j]
print(summary)

tt1 = (10,20, 30, 40)
print(tt1[0])
print(tt1[1] + tt1[2])
print(tt1[1] * tt1[2])


#튜플을 List로 형 변환
mTT = (10,20,30)
print(mTT)
mList = list(mTT)
print(mList)
mList.append(40)
mTT = tuple(mList)
print(mTT)
