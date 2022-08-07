
set1 = {1,2,3,4}
set2 = {3,4,5,6}


print(set1 | set2)
print(set1 & set2)

for i in set1 :
    print(i, end=' ' )
print()


set1.add(8)

#discard 원소삭제
#set1.discard(3)
print(set1.union(set2))
print(set1.difference(set2))
print(set1.intersection(set2))

sMenu = ["A", "B", "C", "D","E","F"]
print(type(sMenu))
sMenu = set(sMenu)
print (type(sMenu))
lMenu = list(sMenu)
print(lMenu)

def toUpper(a) :
    return str(a).upper()


print(toUpper("Hello"+" World"))



#
