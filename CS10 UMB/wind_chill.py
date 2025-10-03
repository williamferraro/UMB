import stdio
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])
# variables^

w = 35.74+0.6215*t+(0.4275*t-35.75)*v**0.16
# The equation used to calculate wind chill

stdio.writeln(w)