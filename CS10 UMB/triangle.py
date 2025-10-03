import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#^Grabbed Integers

if a + b >= c and b + c >= a and c + a >= b:
    #^Used this if statement with or's inbetween to test all scenarios to make sure they are true.
    stdio.writeln('True')
else:
    stdio.writeln('False')
#^else statement to close it out if it came back false.