from random import randint

import stdio
import random

dr = randint(1, 6)

if dr == 1:
    stdio.writeln("     ")
    stdio.writeln("  *  ")
    stdio.writeln("     ")
if dr == 2:
    stdio.writeln("*    ")
    stdio.writeln("     ")
    stdio.writeln("    *")
if dr == 3:
    stdio.writeln("*    ")
    stdio.writeln("  *  ")
    stdio.writeln("    *")
if dr == 4:
    stdio.writeln("*   *")
    stdio.writeln("     ")
    stdio.writeln("*   *")
if dr == 5:
    stdio.writeln("*   *")
    stdio.writeln("  *  ")
    stdio.writeln("*   *")
if dr == 6:
    stdio.writeln("*   *")
    stdio.writeln("*   *")
    stdio.writeln("*   *")
