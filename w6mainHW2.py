"""
@author msj
@since 160406
"""
year=input("User input year : ")

if (year%4==0) and (year%100!=0 or year%400==0):
     print "Leap year"
else:
     print "Not Leap year"

"""
@startuml

title À±³â¸ÂÃß±â 


start

:user input year; 


if (year%4==0) and (year%100!=0 or year%400==0) then (yes)
  :leap year;
else (no)
  :not leap year;
endif


stop

@enduml
"""
if __name__=="__main__":
	main()