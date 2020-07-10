# Understand and plan
# abs() function returns the absolute value
# create empty dictionary "values" to store values while looping through
# create empty list "result" to hold all ints that appear twice
# assuming that positive and negative numbers not duplicated

# execute
def has_negatives(a):
    values = {}
    result = []
    for int in a:
        if abs(int) in values:
            values[abs(int)] += 1
            if values[abs(int)] > 1 and abs(int) not in result:
                result.append(abs(int))
        else:
            values[abs(int)] = 1

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4, 5, -5]))


# reflect
# tests passed so reached MVP
