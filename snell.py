import math
import stdio
import sys

o1 = math.radians(float(sys.argv[1]))
n1 = math.radians(float(sys.argv[2]))
n2 = math.radians(float(sys.argv[3]))

o2 = math.asin(n1*math.sin(o1)/n2)

stdio.writeln(math.degrees(o2))