import random,os

rsp = ['가위', '바위', '보']
dict_rst = {'0': '가위', '1':'바위', '2':'보'}
def RSPcalculator(x, y) :
    if x == y :
        print('비겼습니다')
        return 0
    else :
        if   x == 0 :
            if y == 1 :
                print('졌습니다.')
                return 1
            elif y == 2 :
                print('이겼습니다.')
                return 2
        elif x == 1 :
            if y == 0 :
                print('이겼습니다.')
                return 2
            elif y == 2 :
                print('졌습니다.')
                return 1
        elif x == 2 :
            if y == 0 :
                print('졌습니다.')
                return 1
            elif y == 1 :
                print('이겼습니다.')
                return 2

def RSPMaker() :
    com = random.randint(0,2)
    return com

def score(scoreBoard) :
    w =0
    l =0
    p = 0
    for _ in scoreBoard :
        if _ == 0 :
            p += 1
        elif _ == 1 :
            l += 1
        elif _ == 2 :
            w += 1
    print( '{0}승 {1}패 {2}무'.format( w,l,p))

clearConsole = lambda: print('\n' * 150)
scoreBoard = []

def RSP_Run(num) :
    for i in range (0, num) :
        my = int(input("가위바위보를 입력해주세요 \n가위 : 0 / 바위 : 1 / 보 :2 \n"))
        computer = RSPMaker()
        print("{0}를 냇습니다.".format(rsp[my]))
        print("컴퓨터는 {0} 을 냇습니다.".format(rsp[computer]))
        scoreBoard.append(RSPcalculator(my, computer))
        score(scoreBoard)
    return scoreBoard

