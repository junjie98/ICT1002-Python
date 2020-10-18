import sys

try:
    #  Commandline arguments
    number = int(sys.argv[1])
    option = int(sys.argv[2])

    # Functions
    def double(x):
        return 2*x

    def square(x):
        return x**2

    def cube(x):
        return x**3

    def doTwice(func, number):
        return func(func(number))

    # Check option chosen and outputs accordingly
    if option == 1:
        print(doTwice(double, number))
    elif option == 2:
        print(doTwice(square, number))
    elif option == 3:
        print(doTwice(cube, number))
    else:
        print("It cannot be supported!")

except ValueError:
    print("It cannot be supported!")
    sys.exit(1)
