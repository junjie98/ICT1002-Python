import sys

try:
    #  Commandline arguments
    a = int(sys.argv[1])

    # Functions
    def sum_recursive(x):
        if x == 0:
            return 0
        return x + sum_recursive(x-1)


    def sum_iterative(x):
        total = 0
        for i in range(1, x + 1):
            total = total + i
        return total

    i = sum_iterative(a)
    r = sum_recursive(a)

    # Final Output
    print("The SUM value calculated by recursive is %i and by iterative is %i." % (r, i))

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
