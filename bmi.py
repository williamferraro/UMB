import stdio
import sys
#Used float as per hw instructions
#As well as to help calculate more accurately


w = float(sys.argv[1])
h = float(sys.argv[2])


# I added another variable h2 in order to help the computer solve the problem
# However while working I found that it could be simplified by adding parenthesis in the final line as shown below
#h2 = h**2
#stdio.write(w/h2)

stdio.writeln(w/(h**2))
# So the more simplified code/less code would be just this