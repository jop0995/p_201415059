import turtle

wn=turtle.Screen()

t1=turtle.Turtle()

w=dict()

w=({0:(0,0),1:(0,50),2:(50,50),3:(50,0),4:(0,0)})

def polygone():
    for i in range(1,5):
        t1.goto(w[i])
    for k in range(1,5):
        print w[k]

def lab7():
	polygone()

def main():
	lab7()

wn.exitonclick()