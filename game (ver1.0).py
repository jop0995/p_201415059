import turtle
import math
import time
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
t2.color("yellow")
t2.penup()
t2.goto(0,-250)
t2.setheading(90)
t1.speed(5)
wn.bgcolor("skyblue")
wn.setup(800,600)
result=0

def OpenCoords():
    filehome=open('position.txt')
    coords=list()
    for line in filehome:
        cirpos=line.split(',')
        coords.append([cirpos[0],cirpos[1], cirpos[2],cirpos[3], cirpos[4],cirpos[5].strip()])
    filehome.close()
    return coords
coords=OpenCoords()

def line():
    t1.penup()
    t1.goto(-400,50)
    t1.pendown()
    t1.fd(110)
    t1.penup()
    t1.goto(-210,50)
    t1.pendown()
    t1.fd(190)
    t1.penup()
    t1.goto(20,50)
    t1.pendown()
    t1.fd(210)
    t1.penup()
    t1.goto(240,50)
    t1.pendown()
    t1.fd(160)
    t1.penup()
    t1.goto(-120,300)
    t1.pendown()
    t1.right(90)
    t1.fd(250)
    t1.penup()
    t1.goto(117,300)
    t1.pendown()
    t1.fd(250)
    t1.left(90)
   
	

def square():
    for coord in coords:
        x1=int(coords[0][0])
        y1=int(coords[0][1])
        x2=int(coords[0][2])
        y2=int(coords[0][3])
        x3=int(coords[0][4])
        y3=int(coords[0][5])

    t1.penup()
    t1.goto(x1,y2)
    t1.pendown()
    t1.fillcolor("Black")
    t1.begin_fill()
    for i in range(0,4):
        t1.fd(100)
        t1.right(90)

    t1.end_fill()

def triangle():
    for coord in coords:
        x1=int(coords[0][0])
        y1=int(coords[0][1])
        x2=int(coords[0][2])
        y2=int(coords[0][3])
        x3=int(coords[0][4])
        y3=int(coords[0][5])
    t1.penup()
    t1.goto(x2,y2)
    t1.pendown()
    t1.fillcolor("Brown")
    t1.begin_fill()
    for i in range(0,3):
        t1.right(120)
        t1.fd(100)

    t1.end_fill()
        
def polygone():
    for coord in coords:
        x1=int(coords[0][0])
        y1=int(coords[0][1])
        x2=int(coords[0][2])
        y2=int(coords[0][3])
        x3=int(coords[0][4])
        y3=int(coords[0][5])
    t1.penup()
    t1.goto(x3,y3)
    t1.pendown()
    t1.fillcolor("Red")
    t1.begin_fill()
    for i in range(0,5):
        t1.fd(70)
        t1.right(72)

    t1.end_fill()
    
        
def do():
    line()
    square()
    triangle()
    polygone()

def squp():
    (x,y)=t2.pos()
    global result
    if -300<=x<-200 and 100<=y<=200:
        result=result+1
        print(" point total %d !" % result)
        t2.goto(0,-200)

def trip():
    (x,y)=t2.pos()
    global result
    if -50<=x<50 and 180<=y<=200:
        result=result+3
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if -35<=x<35 and 155<=y<=180:
        result=result+3
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if -15<=x<15and 135<=y<=155:
        result=result+3
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if -5<=x<5 and 100<=y<=135:
        result=result+3
        print(" point total %d !" % result)
        t2.goto(0,-200)

def polyp():
    (x,y)=t2.pos()
    global result
    if 200<=x<270 and 188<=y<=200:
        result=result+5
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 192<=x<278 and 166<=y<=188:
        result=result+5
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 186<=x<286 and 144<=y<=166:
        result=result+5
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 180<=x<290 and 122<=y<=144:
        result=result+5
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 200<=x<250 and 100<=y<=122:
        result=result+5
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 220<=x<240 and 90<=y<=100:
        result=result+5
        print(" point total %d !" % result)
        t2.goto(0,-200)

def linep():
    (x,y)=t2.pos()
    global result
    if -400<=x<-290 and 45<=y<=56:
        result=result-1
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if -210<=x<-20 and 45<=y<=56:
        result=result-1
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 20<=x<230 and 45<=y<=56:
        result=result-1
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 240<=x<400 and 45<=y<=56:
        result=result-1
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if -125<=x<-114 and 50<=y<=300:
        result=result-1
        print(" point total %d !" % result)
        t2.goto(0,-200)
    if 110<=x<126 and 50<=y<=300:
        result=result-1
        print(" point total %d !" % result)
        t2.goto(0,-200)

    
do()
  
def h1():
    t2.forward(10)
    squp()
    trip()
    polyp()
    linep()
    
   

def h2():
    t2.left(45)

def h3():
    t2.right(45)

def h4():
    t2.back(30)  
 
wn.onkey(h1, "Up")
wn.onkey(h2, "Left")
wn.onkey(h3, "Right")
wn.onkey(h4, "Down")
wn.listen()

turtle.mainloop()
