import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.shape("turtle")
t2.penup()
wn.setup(500,500)
def square():
    t1.penup()
    t1.goto(-150,200)
    t1.pendown()
    for i in range(0,4):
        t1.fd(40)
        t1.right(90)

def triangle():
    t1.penup()
    t1.goto(25,200)
    t1.pendown()
    for i in range(0,3):
        t1.right(120)
        t1.fd(50)
        
def polygone():
    t1.penup()
    t1.goto(150,200)
    t1.pendown()
    for i in range(0,5):
        t1.fd(30)
        t1.right(72)
        
def do():
    square()
    triangle()
    polygone()

do()

def h1():
    t2.fd(30)
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

if __name__=="__main__": 
 	main() 
