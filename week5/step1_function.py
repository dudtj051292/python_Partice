def starcount(num) :
    count = 0
    for i in range(1, num+1) :
        star = ""
        for _ in range(i) :
            star += "*"
            count += 1
        print(star)

    def inlineStarCount() :
        return count
    return inlineStarCount

# inlineStarCount = starcount(int(input("숫자를 입력하세요 : ")))
# print("star 갯수 : ", inlineStarCount())


def calc_func(a,b) :
    x = a
    y = b

    def plus():
        p = x+y
        return p
    def minus() :
        m = x-y
        return m
    return plus, minus


class Subject:
    name =''
    score = ''
    def setName(self, t_name):
        self.name = t_name
    def setScore(self, t_score):
        self.score = t_score
    def getName(self):
        return self.name
    def getScore(self):
        return self.score
    def __init__(self, t_name, t_score):
        self.name = t_name
        self.score = t_score

class Student :
    name = ''
    major = ''
    grade = ''
    subject = []
    # 생성자 (Constructor)

    def __init__(self, t_name, t_major, t_grade):
        self.name = t_name
        self.major = t_major
        self.grade = t_grade

    # method(함수)
    # setter
    def setName(self, t_name):
        self.name = t_name
    def setMajor(self, t_major):
        self.major = t_major
    def setGrade(self, t_grade):
        self.grade = t_grade
    def setSubject(self, name, score):
        Subject(name, score)
    # getter
    def getName(self):
        return self.name


    def display(self):
        print("학생명 : [{}] 전공 : [{}] 학년 : [{}] ".format(self.name, self.major, self.grade))



std2 = Student("이민지" , "산업디자인학부 융합디자인전공", "1학년")
std2.display()