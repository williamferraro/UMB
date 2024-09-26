import stdio
import sys

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])
q = 1-p
#Used given variables

p1 = float(1-(p/q)**n2)/(1-(p/q)**(n1+n2))

p2 = float(1-(q/p)**n1)/(1-(q/p)**(n1+n2))

#Both equations used for both Player 1 and Player 2^

stdio.writeln(str(p1) + ' ' + str(p2))
#Used the str function to convert the int/float answers
#So that I could add them together as strings and the final answer would have a space