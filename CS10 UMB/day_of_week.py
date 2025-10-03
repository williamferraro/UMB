import stdio
import sys


m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])
#variable given within problem
#used int function to remove the float/decimal places within result

y1 = y-(14-m)//12
x = y1+y1//4-y1//100+y1//400
m1 = m+12*((14-m)//12)-2
# ^The math to get are answer wrote out
#Used multiple different variables as well as split up the math to ensure
#that the math was properly executed by program.

d1 = (d+x+31*m1//12)%7


stdio.writeln(d1)
