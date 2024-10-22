import stdio
import sys
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

y1 = y-(14-m)//12
x = y1+y1//4-y1//100+y1//400
m1 = m+12*((14-m)//12)-2

d1 = (d+x+31*m1//12)%7
#Used the given equations to get the calculations for the days of the week

if d1 == 0:
    stdio.writeln('Sunday')
if d1 == 1:
    stdio.writeln('Monday')
if d1 == 2:
    stdio.writeln('Tuesday')
if d1 == 3:
    stdio.writeln('Wednesday')
if d1 == 4:
    stdio.writeln('Thursday')
if d1 == 5:
    stdio.writeln('Friday')
elif d1 == 6:
    stdio.writeln('Saturday')
#Then used an if statement to check if the answer was equal to a day
#Used elif to signify the end of the check