import stdio
import sys

n = int(sys.argv[1])

if n % 2 == 0:
    stdio.writeln(False)
else:
    stdio.writeln(True)