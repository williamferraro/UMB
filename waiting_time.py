import math
import stdio
import sys

j = float(sys.argv[1])
t = float(sys.argv[2])
# Used the provided variables

wt = math.e**(-j*t)
# Used wt as the variable for Waiting Time
#Used math.e from the Math import to represent e from the equation:
# p=e**-j(representing number of events per units of time)*t(to represent time)

stdio.writeln(wt)


