import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawPolygonAt(size, pos):
    
    tracks=list()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    
    for i in range(1,5):
            t1.fd(size)
            t1.right(90)
            tracks.append(t1.pos())
    return tracks
        

            
def lab7():
    mytracks=drawpolygonAt(size,pos)
    print mytracks
def main():
    lab7() 

if __name__ == '__main__': 
	main() 
