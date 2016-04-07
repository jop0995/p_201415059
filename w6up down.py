"""
@author msj
@since 20160407

"""

import random

rn = random.randrange(1, 101, 1)
num = -1

t_cnt = 0

print("strat")
while ( rn != num ):
	num = int(input("number input"))
	if (num > rn):
        	print("Down")
    	elif (num < rn):
        	print("Up")
	t_cnt+=1 
print(" good job")
wn=raw_input()

"""
Diagram
@startuml

title Up and Down
:user input range number(==rn);
:computer choose number in range;


start

while (r1=s1)  is (no)
if(s1>r1)
  :print down;
elseif(s1<r1)
  :print up;
else
  :print error;
endif
endwhile
stop



@enduml
"""
if __name__=="__main__":
	main()
	