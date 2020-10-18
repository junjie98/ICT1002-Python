import sys
import re

try:
    # Commandline arguments
    list1 = [str(c) for c in sys.argv[1].split(',')] 
    list2 = [str(c) for c in sys.argv[2].split(',')]

    # Join string
    candidate = ','.join(list1)
    pattern = ','.join(list2)
    count = 0
    pattern = ("(?=" + pattern + ")")

    # Counts the number of times a pattern is found
    if re.findall(pattern, candidate):
        for match in re.finditer(pattern, candidate):
            count += 1
        print("Pattern appears %i time!" % count)
    else:
        print("Pattern appears %i time!" % count)

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
