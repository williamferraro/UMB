import stdio
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])
w = float(35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v**0.16)
# Used the given variables as well as defined the wind equation

if t > 50:
    stdio.writeln("Value of t must be ≤ 50 F")
elif v <= 3:
    stdio.writeln("Value of v must be > 3 mph")
# used an If and elif loop to check to make sure given variables were within given parameters

else:
    stdio.writeln(w)
#Used the last line to print answer if all conditions were met