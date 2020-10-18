import sys

try:
    #  Commandline arguments
    a = str(sys.argv[1])

    # Function
    def elf_recursive(x, pattern, result=True):
        if result:
            x, pattern = map(sorted, (x, pattern))
            result = False
        if not pattern:
            return True
        try:
            index = x.index(pattern[0])
        except ValueError:
            return False
        return elf_recursive(x[index + 1:], pattern[1:], result)


    elfish = "elf"
    w = elf_recursive(a, elfish)

    # Output
    if w:
        print("%s is one elfish word!" % a)
    else:
        print("%s is not an elfish word!" % a)

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
