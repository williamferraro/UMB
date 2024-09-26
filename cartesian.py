import math
from math import radians

import stdio
import sys


r = float(sys.argv[1])
O = math.radians(float(sys.argv[2]))
#math.radians to convert float to radians
x = r*math.cos(O)
y = r*math.sin(O)
#^The Given equations

stdio.writeln(str(x)+' '+str(y)+'\n')