

class Car :
    cc = 0
    door = 0
    carType = None

    def __init__(self, cc, door, carType):
        self.cc = int(cc)
        self.door = int(door)
        self.carType = carType

    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s 이다."
              %(self.cc, self.door, self.carType ))

suv = Car("2000" , "4" , "suv")

suv.display()