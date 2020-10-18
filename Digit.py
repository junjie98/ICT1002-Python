import sys

try:
    #  Commandline arguments
    a = int(sys.argv[1])

    # Functions
    def digit(x):
        if x < 1:
            return 0
        else:
            b = x / 10
            return 1 + digit(b)


    def digit_iterative(x):
        i = 0
        while x > 0:
            x //= 10
            i += 1
        return i

    i = digit_iterative(a)
    r = digit(a)

    # Final Output
    print("The number of digit(s) calculated by recursive is %i and by iterative is %i." % (r, i))

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
