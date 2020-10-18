import sys

try:
    # Commandline arguments
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    # Calculate the average
    average = (a + b + c) / 3
    average = round(average, 2)

    # Print Output
    print("Average: " + "%.2f" % average)

# Catch Error
except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
