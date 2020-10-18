import sys

try:
    #  Commandline arguments
    sales = [int(c) for c in sys.argv[1].split(',')]
    scaler = int(sys.argv[2])

    # Functions
    def scale(list1, x):
        return list(map(lambda x: x * scaler, list1))

    def sort(list1) -> object:
        return sorted(list1, key=lambda x: x % 10)

    def goodSales(list1):
        average = sum(list1) / len(list1)
        return list(filter(lambda x: x > average, sales))

    scaledno = scale(sales, scaler)
    sortedno = sort(sales)
    salesno = goodSales(sales)

    # Final Output
    print(str("The scaled number is: %s The sorted sales numbers "
              "are: %s The good sales numbers are: %s") %(scaledno, sortedno, salesno))

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
