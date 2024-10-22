import math

import stdio
import sys

p = int(sys.argv[1])
q = int(sys.argv[2])
#Grabbed input from user^

gcd = math.gcd(p, q)
#I found that python uses the gcd math function

stdio.writeln(gcd)