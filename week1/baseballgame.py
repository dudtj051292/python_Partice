import random

try:
    def start():
        a =  [random.randint(1, 9),random.randint(1, 9),random.randint(1, 9)]
        print(a)
        return a

    def baseballCheck(a, b) :
        strikeCnt = 0
        for i in range(0, len(a)) :
            print(i, a[i], b[i])
            if a[i] == int(b[i]) :
                strikeCnt += 1

        ballCnt = 0

        for i in a :
            for j in b :
                if i == j  :
                    ballCnt +=1

        if strikeCnt == 3 :
            print('HOMERUN!!!!')
            return True
        else :
            print(f'[{strikeCnt}] Strike [{ballCnt}] Ball')
            return False

    result = start()
    isCorrect = True

    while True :
        iList = []
        iList = input('숫자 3개를 입력하세요( 띄어쓰기로 구분 해주세요) ').split()
        if baseballCheck(result, iList):
            break



except TypeError as ex :
    print(ex)
except ValueError as ex :
    print(ex)

