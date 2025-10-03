from random import random

import stdio
import random
import sys



n = int(sys.argv[1])


dr = random.uniform(1, n)

dr2 = random.uniform(1, n)

td = dr + dr2

stdio.writeln(int(td))