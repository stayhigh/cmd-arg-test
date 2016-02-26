import itertools
import sys

usage = """
Usage: python cmdargs_combinations.py <cmdargs_str> <the number of elements>

INPUT:
<cmdargs_st> => "-a -b -c -d -e"
<the number of elements> => 3

OUTPUT:
-a -b -c
-a -b -d
-a -b -e
-a -c -d
-a -c -e
-a -d -e
-b -c -d
-b -c -e
-b -d -e
-c -d -e
"""

if len(sys.argv) < 2:
    print usage
    exit()
elif len(sys.argv) < int(sys.argv[-1]):
    print "impossible picking number"
    exit()

cmdargs_list = sys.argv[1:len(sys.argv) - 1]
element_num = int(sys.argv[-1])
outcomes = []

for element in itertools.combinations(cmdargs_list, element_num):
    outcomes.append(element)

for outcome in outcomes:
    each_record = " ".join(list(outcome))
    print each_record