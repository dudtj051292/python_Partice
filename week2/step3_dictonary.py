items= {"coffee":2000 , "latte":2500 , "ade":3000 , "tea":2300 }
print(items)
print(type(items)) # <class 'dict'>
print(items["coffee"])
print(items.keys())
print(items.values())

# update
items["coffee"] = 2500
print(items["coffee"])

# delete
#del items["ade"]
#print(items)

# insert
items["bear"]=5000
print(items)


# contains
print("ade" in items)
print("coffee" in items)
for k in items.items() :
    print(k)

print(items.get("coffee"))

#dict 전체 내용 삭제
# items.clear()
# print(items)

summary = 0
orderlist = {}
while True :
    menu = input("메뉴를 입력해주세요 (종료 :exit) : ")
    if(menu in items) :
        print("{0}을 주문하셧습니다.".format(menu))
        summary += items[menu]
        print("현재 주문상품및 금액은 {0} [{1}]원 입니다. 총 주문 금액 {2}".format(menu, items[menu],summary))
        orderlist[menu] = orderlist.get(menu, 0 )+1;
    elif (menu == "exit") :
        break
    else:
        print("없는 메뉴입니다.")

print("총 주문 금액은 %d"%summary)
print("주문내역서 : ")
print(orderlist)



