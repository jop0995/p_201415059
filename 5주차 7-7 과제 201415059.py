"""  
@author msj  
date 2016/4/04  
 """  
   
"""  
BMI CONVERT   
"""  
import turtle  
wn=turtle.Screen()  
t1=turtle.Turtle()  
def lab5():  
w1=raw_input("input your weight: ")  
h1=raw_input("input your height: ")  
weight=float(w1)  
height=float(h1)  
bheight=height/100.  
Bmi=weight/(bheight*bheight)  
if(Bmi<18.5):  
	print "low weight"  
elif(18.5<=Bmi<25):  
	print "normal"  
elif(25<=Bmi<30):  
	print "mild obesity"  
elif(30<=Bmi):  
	print "high obesity"  
else:  
    	print "Error"  
t1.write("201415059 윤주석 과제 끝!")  
lab5()  
def main():  
lab5()  
  
  
wn.exitonclick() 
