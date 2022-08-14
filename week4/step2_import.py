import turtle
import math

t = turtle.Turtle()

def ractangle(len):
    for i in range(4) :
        t.forward(len)
        t.left(90)

def trangle(len) :
    for i in range(3) :
        t.forward(len)
        t.left(120)


def spring(len) :
    theta = 180
    while True :
        t.forward(10)
        t.left(math.cos(theta) * math.sin(theta))
        print(t.position)

len=50

spring(len)
