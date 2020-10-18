import sys

try:
    # Commandline arguments
    unit = str(sys.argv[1])
    height = float(sys.argv[2])
    weight = float(sys.argv[3])

    # Selection of units & calculation
    # BMI = weight/height (metric units)
    # BMI = 703*(weight/height) (us units)
    if unit == "metric":
        bmi = weight / (height * height)
    elif unit == "imperial":
        bmi = 703 * (weight / (height * height))
    else:
        print("Your input is invalid!")

    # BMI decision maker
    if bmi < 16:
        print("%0.2f" % bmi + "\t Severe Thinness")
    elif 16 <= bmi <= 17:
        print("%0.2f" % bmi + "\t Moderate Thinness")
    elif 17 <= bmi <= 18.5:
        print("%0.2f" % bmi + "\t Mild Thinness")
    elif 18.5 <= bmi <= 25:
        print("%0.2f" % bmi + "\t Normal")
    elif 25 <= bmi <= 30:
        print("%0.2f" % bmi + "\t Overweight")
    elif 30 <= bmi <= 35:
        print("%0.2f" % bmi + "\t Obese Class I")
    elif 35 <= bmi <= 40:
        print("%0.2f" % bmi + "\t Obese Class II")
    elif bmi > 40:
        print("%0.2f" % bmi + "\t Obese Class III")
    else:
        print("Your input is invalid!")

# Catch Error
except IndexError:
    print("Your input is invalid!")
    sys.exit(1)
