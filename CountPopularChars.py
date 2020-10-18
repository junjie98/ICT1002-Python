import sys
from collections import Counter

try:
    # Commandline arguments
    a = str(sys.argv[1])

    # Take in String and Lowercase them
    lowercase = a.lower()
    # Sorts
    sorted_lowercase = sorted(lowercase)
    # Count the 5 most common characters
    counts = Counter(sorted_lowercase).most_common(5)
    print(','.join(['{0}:{1}'.format(value, count) for value, count in counts]))

except ValueError:
    print("Your input is invalid!")
    sys.exit(1)
