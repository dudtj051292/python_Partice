
class Memo :
    name = ''
    msg = ''
    def getMemo(self):
        return self.msg
    def setMemo(self, msg):
        self.msg = msg

    def __init__(self, name, msg) :
        self.name = name
        self.msg = msg
        return


class MemoList :
    memos = []
    def setMemos(self, name, msg):
        self.memos[name] = Memo(name, msg)
    def getMemos(self, memonum):
        print(len(self.memos))
        if len(self.memos) == 0 :
            print("메모가 없습니다. ")
            self.memos.append( Memo(input("메모 이름을 입력하세요 : "), input("메시지를 입력해주세요 : ")))
            memonum=0
            return
        if(len(self.memos) <= memonum) :
            print("없는 메모입니다.")
            self.memos.append( Memo(input("메모 이름을 입력하세요 : "), input("메시지를 입력해주세요 : ")))
            return self.memos[memonum]
        else :
            return self.displayOne(memonum)
    def displayOne(self, memonum):
        print("제목 : ", self.memos[memonum].name )
        print("내용 : ", self.memos[memonum].msg)

    def display(self) :
        if(len(self.memos) == 0 ):
            print("없습니다.")
        for memo in self.memos :
            print( self.memos.index(memo) , "번 메모 - 제목 : " ,memo.name )
MemoList = MemoList()
while True :
    MemoList.display()
    MemoList.getMemos(int(input("메모 번호를 입력해주세요(없는경우 새로 생성됩니다) : ")))