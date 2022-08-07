import random

#range (시작값, 끝값+1, 증가값)
# 시퀀스 변수 대신 _ 사용 가능
# for _ in range(1,101, 5) :
#     print(_)
#
# for _ in range(101, 1, -5) :
#     print(_)
#
# hap = 0
# for _ in range(1,101) :
#     if _ % 5 == 0 :
#        hap += _
# print("hap : {0}".format(hap))
#
# even =0;
# odd = 0;
# total = 0
# for _ in range(1,101) :
#     total += _
#     if _ % 2 == 0 :
#        even += _
#     else :
#         odd += _
# print("총계 {2} ... 짝수 : {0} / 홀수 {1}".format(even, odd,total))


#dan = int(input("구구단 단수를 입력해 주세요 : "))
# dan = 1
# for dan in range(1,10) :
#     for _ in range(1, 10) :
#         print("{0} x {1} = {2}".format(format(dan,"2"), format(_, "1") , format(dan * (_) ,"3")) )
#
# sum = 0
# cnt = 0
# for dice1 in range(1,7) :
#     for dice2 in range (1,7) :
#        if dice1 + dice2 == 6 :
#            print("(%d, %d)" %(dice1,dice2))
#            cnt += 1
# print(cnt)



# passwd = input("사용하실 비밀번호를 입력해주세요 : ")
# inputval = 0
# while True :
#     inputval = input("비밀번호를 입력해주세요 : ")
#     if inputval == passwd :
#         print( "비밀번호가 일치합니다. ")
#         break;
#     else :
#         print( "비밀번호가 일치하지않습니다. ")

lotto = []
while len(lotto) != 6 :
    num = random.randint(1,45)
    if(lotto.__contains__(num) == False ) :
        lotto.append(num)

lotto.sort()
print(lotto)


a = [1,2,3,4,5,6,7]
b= []
for num in a :
    print(num , end = "\t")
    if num %2 == 0 :
        b.append(num *3)


print(b)

result = [num*3 for num in a if num*3 %2 == 0]

print(result)

# 1~100 사이의 수중에 2의배수만 담기는 list
evenList2 = [_ for _ in range(1,101) if _ %2 == 0 and _ %5 == 0 ]
print ("evenList : ")
print(evenList2)


cnt = int(input("몇번 반복하시겠습니까? : " ))

for _ in range(cnt) :
    print(format("*" * (cnt -_ ), format("{0}".format(cnt) ) ) ,end= "")
    print(format("*" * (_+1)    , format(">{0}".format(cnt))  ))


# slicing letter[start:end] start, end 생략가능

# append(val) - 맨앞에 추가

# insert( idx , val) idx위치에 val 추가

# remove(val) del[idx]

slist = ["kiwi", "banana" , "pear"]
slist.append("orange")
slist.append("peach")
print(slist)
slist.insert(3, "mange")
print(slist)
slist.remove("orange")
print(slist)
del slist[2]
print(slist)

print(slist.index("peach"))