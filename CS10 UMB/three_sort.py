import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
#Used To grab Input from User

L = max(a, b, c)
#Used the max function to Find the largest Integer
S = min(a, b, c)
#Used the min function to find the smallest Integer
M = int((a + b + c) - S - L)
#To find the Middle number I simply added all the given integers together
#I then subtracted both the largest and smallest integers from the sum to find the Middle number

stdio.writeln(str(S)+' '+str(M)+' '+str(L))