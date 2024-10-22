import stdio
import sys

n = int(sys.argv[1])
if n == 1:
    return 1
    stdio.writeln(n)

else:
    SP = sum(i**n for i in range(1,n+1))

stdio.writeln(SP)