import copy

movie = {'광해' : [9.24, 1200], '공작' : [7.86, 500] , '관상' : [8.01, 900] }

for item in movie.items():
    print(item)

for k, v in movie.items():
    print(k , v)

# 평점 8 이상인 영화 제목과 누적관객수 만들기
summary = 0;
for key, value in movie.items():
    if(value[0] >= 8.0):
        summary += value[1];
        print("영화 : {0} 평점 : {1} 누적관객수 : {2}".format(key, value[0], summary))


foods = {"떡볶이":"오뎅",
         "짜장면":"단무지",
         "라면"  : "김치",
         "피자"  : "피클",
         "맥주"  : "땅콩",
         "치킨"  : "치킨무",
         "삼겹살": "소주"}

print(foods)

# 좋아하는 음식은?

#while(True) :
#    myFood = input("좋아하는 음식은? : ")
#    if myFood in foods :
#        print("{0}에는 {1}이죠".format(myFood, foods.get(myFood)))
#    elif myFood == "끝"  :
#        break
#    else :
#        print("없는 메뉴입니다...")



# 단어 빈도수 구하기
charset = ['Banana' , 'Apple', 'Strawberry', 'Mango', 'Strawberry','Strawberry','Strawberry']
myWordCountSet = {}

for key in charset :
    #if(key in myWordCountSet) :
    #    myWordCountSet[key] +=1
    #else :
    #    myWordCountSet[key] = 1

    myWordCountSet[key] = myWordCountSet.get(key, 0) +1
    print(key)
    # page 101
print("set : {0}".format (myWordCountSet))


# [실습] 문자 빈도수 구하기
charset = ['abc' , 'code','band', 'code', 'band', 'abc']
wc = {}

for key in charset :
    wc[key] = wc.get(key , 0) +1
    print('max = ', max(wc, key=wc.get))
    print(key)

print('max = ', max(wc, key=wc.get))

a= [10,20]
print(id(a))
b = a
print(id(b))
a[0] = 30
print(a)
print(b)


name = ['홍길동' , '이순신', '강감찬']
name2 = copy.deepcopy(name)
print(name)
print(name2)


#1~100까지의 랜덤수 10개 뽑기
import random

ranList =[]
for _ in range(0,10):
    ranList.append(random.randint(1,100))

print(ranList)

# max , min
max = min = ranList[0]
for i in ranList :
    if  max < i :
        max = i
    if min > i :
        min = i

print("최대값 : {0} / 최소값 : {1} ".format(max, min))


# sort 1) 오름차순

for i in range(0, len(ranList)) :
    for j in range(0,i):
        if(ranList[i] > ranList[j]) :
            temp = ranList[i]
            ranList[i] = ranList[j]
            ranList[j] = temp
    print( "{0} : {1}".format(i,ranList))


print(ranList)


ranList2 =[]
