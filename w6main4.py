j=list()

def sumlist(j):
     for i in range(0.1001):
         if i%4==0 and i%5!=0:
             j.append(i)
     sum=0
     for i in range(len(j)):
         sum=sum+j[i]
     return sum


def main():
     print sumlist(j)
main()
raw_input("enter to end")