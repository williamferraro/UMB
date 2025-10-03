import math
import random
import stdio
import random
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

x1 = random.uniform(a, b)
x2 = random.uniform(a, b)
x3 = random.uniform(a, b)

u = (x1 + x2 + x3)/3
var = ((x1-u)**2 + (x2-u)**2 + (x3-u)**2)/3
a = math.sqrt(var)

stdio.writeln(str(u) +' '+ str(var)+' '+ str(a))