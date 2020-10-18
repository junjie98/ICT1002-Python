import sys

try:
    # Commandline arguments
    workinghours = int(sys.argv[1])
    normalrate = int(sys.argv[2])
    overtimerate = int(sys.argv[3])

    # If more than 1 week of hours it is invalid
    if workinghours > 168:
        print("Your input is invalid!")

    # Calculating no OT
    elif workinghours <= 40:
        normalpayment = normalrate * workinghours
        extrasalary = 0.00
        totalsalary = normalpayment + extrasalary
        print("Normal Salary:%.2f, Extra Salary:%.2f, Total Salary:%.2f" % (normalpayment, extrasalary, totalsalary))

    # Calculating OT + Normal Hours
    elif workinghours > 40:
        overtime = workinghours - 40
        normalpayment = normalrate * 40
        extrasalary = overtimerate * overtime
        totalsalary = normalpayment + extrasalary
        print("Normal Salary:%.2f, Extra Salary:%.2f, Total Salary:%.2f" % (normalpayment, extrasalary, totalsalary))

    else:
        print("Your input is invalid!")

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
