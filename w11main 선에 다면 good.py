import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t1.penup()
t1.shape("turtle")
t2=turtle.Turtle()
t2.shape("circle")
def Line():
	t2.penup()
	t2.goto(-150,200)
	t2.pendown()
	t2.fd(400)


def up():
	t1.fd(50)
def right():
	t1.right(45)
def left():
	t1.left(45)
def back():
	t1.back(50)
def mousegoto(x,y):
	t1.setpos(x,y)
	(x,y)=t1.pos()
	if -150<x<250 and 200<y<210:
		print "good"

def addkey():
	wn.onkey(up,"Up")
	wn.onkey(right,"Right")
	wn.onkey(left,"Left")
	wn.onkey(back,"Down")
	wn.onkey(wn.bye, "q")

def addMouse():
 	wn.onclick(mousegoto)

Line()
addMouse()
addkey()
wn.listen()
turtle.mainloop()
