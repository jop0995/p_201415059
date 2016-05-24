import os
mydir=os.getcwd()

def homework_1():
    filename=raw_input("Input your filename(ex:python.txt):")
    myfilename=os.path.join(mydir,filename)
    try:
        my=open(myfilename, 'r')
        contents=my.readlines()
        for i in range(0,len(contents)):
            if contents[i].find('Python') >= 0:
                print contents[i]
        my.close()
    except IOError as e:
        print e

def homework_2():
    filetwo=open('output.txt', 'w')
    line1='first line\n'
    filetwo.write(line1)
    line2='second line\n'
    filetwo.write(line2)
    line3='third line'
    filetwo.write(line3)
    filetwo.close()
    myfiletwo=open('output.txt', 'r')
    contentstwo=myfiletwo.readlines()
    for a in range(0,len(contentstwo)):
        if contentstwo[a].find('l') >= 0:
            result = contentstwo[a].split()
        for b in range(0,len(result)):
            if result[b].find('l') >= 0:
                print result[b].upper()
    myfiletwo.close()
    
def lab12():
    print "Homework 1"
    homework_one()
    print "Homework 2"
    homework_two()

def main():
    lab12()
    raw_input()

if __name__=="__main__":
    main() 