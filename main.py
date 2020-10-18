import sys
import myMath

try:
    # Commandline arguments
    l = []
    for a in sys.argv[1:]:
        for part in a.split(","):
            if part.strip():
                l.append(int(part.strip()))

    # Declaring all variables
    difference = 0
    summation = 0
    summationall = 0
    even = 0
    zerolist = []

    min = myMath.minimum(l)
    max = myMath.maximum(l)

    # Difference of big and small
    difference = myMath.subtraction(max, min)

    # Summation of big and small
    summation = myMath.add(max, min)

    # Summation of all input
    summationall = myMath.sumTotal(l)

    # Even numbers
    evennum = myMath.evenNum(l)
    even = len(evennum)

    # Set to zero
    if min < 5:
        zerolist = myMath.clear(l)
    else:
        zerolist = l

    strlist = str(zerolist)
    # Final Output
    print(
        "The  difference  is:%i  The  summation  is:%i  The  summation  of  all  input is:%i The number of even "
        "numbers is:%i The values in the list are: %s" % (
            difference, summation, summationall, even, zerolist))

except ValueError:
    print("Please enter valid integers.")
    sys.exit(1)
