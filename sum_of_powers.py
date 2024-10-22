import stdio
import sys

n = int(sys.argv[1])
k = int(sys.argv[2])
#Grabbed argument from user^
Sm = sum(i**k for i in range(1, n+1))
#Used for i in range to use the n variable to loop until the given set was complete

stdio.writeln(Sm)
#Printed result^