import stdio
import sys

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
#variables given/requested

G = float(6.674*10**-11)
# Separate calculation for G

stdio.writeln(G*m1*m2/r**2)
# This is the equation written out^
