import random
import sys
from random import randint, random

import stdio
import random

base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
#created 2 lists for the program to go through at random

rb = random.choice(base)
rs = random.choice(suits)
#Used the random choice function to run through the list and pick 2 random variables from each

stdio.writeln( str(rb) + ' of ' + rs )
#converted the first one to a string because it has a choice to pick a random integer
#which cannot be "added"  together with another string