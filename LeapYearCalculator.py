import sys

try:
    # Commandline arguments
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Declaring variables
    numleap = 0
    leapyear = []
    # Unpack range into list
    yearlist = [*range(a, b + 1)]

    for year in yearlist:
        if ((year % 400) == 0) or (year % 4 == 0) and (year % 100 != 0):
            numleap += 1
            leapyear.append(year)

    # Final Output
    listtostr = ', '.join(str(e) for e in leapyear)
    print("The number of Leap Years is %i, the Leap Years are %s" % (numleap, listtostr))

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
