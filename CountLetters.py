import sys
from collections import Counter

try:
    # Commandline arguments
    l = []
    for a in sys.argv[1:]:
        for part in a.split(","):
            if part.strip():
                l.append(str(part.strip()))


    # Functions
    def letter_count(str):
        counts = Counter(str)
        counts = dict(counts)
        return counts


    def double_count(str1, str2):
        str3 = str1 + str2
        dcounts = Counter(str3)
        dcounts = dict(dcounts)
        return dcounts


    def various_count(*str):
        list1 = str
        str1 = ''.join(list1)
        for x in str1:
            vcounts = Counter(str1)
            vcounts = dict(vcounts)
            return vcounts


    unsorted_total = various_count(*l)
    # Sorting in reverse
    sorted_total = sorted(unsorted_total.items(), reverse=True)
    # Final Output
    for item in sorted_total:
        print("%s:%d" % (item[0], item[1]), end=" ")

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
