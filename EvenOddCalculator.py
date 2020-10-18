import sys
from statistics import mean

try:
    # Commandline arguments
    l = []
    for a in sys.argv[1:]:
        for part in a.split(","):
            if part.strip():
                l.append(int(part.strip()))

    # Declaring all variables
    even = 0
    odd = 0
    evensum = 0
    oddsum = 0
    difference = 0
    average = 0

    # Calculate even and odd sum
    for num in l:
        if num % 2 == 0:
            evensum += num
        else:
            oddsum += num

    # Calculate difference
    number = sorted(map(int, l))
    difference = number[-1] - number[0]

    # Calculate how many even and odd
    for num in l:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    # Centered Average
    l.sort()
    average = mean(l[1:-1])

    # Output
    print(
        "The sum of all even numbers is %i, the sum of all odd numbers is %i, the difference between the biggest and "
        "smallest number is %i, the total number of even numbers is %i, the total number of odd numbers is %i, "
        "the centered average is %i." % (
            evensum, oddsum, difference, even, odd, average))

except ValueError:
    print("Please enter valid integers.")
    sys.exit(1)
