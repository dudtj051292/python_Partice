import time

bankAccountList = {}
def bankSystem() :
    # 잔액확인

    def createAccount(accountID):
        global bankAccountList
        if(bankAccountList.get(accountID) == None):
            bankAccountList[accountID] = 0

    def getAccountInfo(accountID) :
        print('accountID =', accountID)
        print('bankAccountList =', bankAccountList)
        print('accountinfo =', bankAccountList.get(accountID))
        def balance() :
            print('잔액 {0}'.format(bankAccountList.get(accountID)))


        def deposit(money) :
            nonlocal accountID
            balance = bankAccountList.get(accountID)
            bankAccountList[accountID] += money
            print("{0}원 입금".format(money))

        def withdraw(money) :
            nonlocal accountID
            balance = bankAccountList.get(accountID)
            if balance < money  :
                print('잔액보다 큰 돈은 출금 할 수 없습니다')
            else :
                bankAccountList[accountID] -= money
                print("{0}원 출금".format(money))

        return balance , deposit, withdraw

    return createAccount, getAccountInfo


createaccount, getAccountInfo = bankSystem()

createaccount('1100')
print(bankAccountList)
balance, deposit, withdraw = getAccountInfo('1100')
deposit(1000)
balance()
createaccount('1101')
balance, deposit, withdraw = getAccountInfo('1101')
deposit(3000)

print(bankAccountList)

# balance, deposit, withdraw = bankSystem()
# balance()
# deposit(10000)

score = 0
movie = ["Topgun", "Hansan", "Avengers", "Avator", "Titanic"]
print(len(movie))
def wordGame () :
    start = time.time()
    end = wordgame_Run()
    print("총 플레이 시간 : ", end-start )


def wordgame_Run() :
    global score
    movielen = len(movie)
    while score < movielen :
        input_movie = input("input movie name : ")
        if( movie.count(input_movie) ==1 ) :
            score +=1
            print("Correct! nowScore : ", score)
            movie.remove(input_movie)
        else :
            print("inCorrect! ")
    return time.time()
a

# wordGame()


# 외부함수 리턴값으로 내부함수 지정
def a() :
    print('a함수')
    def b ():
        print('b함수')
    return b
z = a()
# z() #일급합수


data = list(range(1,101))

def calc_data(data) :
    # 합계 inner 함수
    def tot () :
        tot_val = sum(data)
        return tot_val
    def avg(tot_val) :
        avg_val = tot_val/ sum(data)
        return avg_val

    return tot, avg # 클로져함수

t,a = calc_data(data)
print('total = ', t())
print('avg = ', a(t()))


def A() :
    x = 10
    def B():
        nonlocal x
        x=20
    B()
    print(x)


A()


def main_func(num) :
    num_val = num

    def getter() :
        return num_val

    def setter(value) :
        nonlocal num_val
        num_val =value

    return getter, setter


