# understand and plan:
# create dictionary values = {} to index values
# create list result = [] to append matching integers
# if already in result list, count. If count equals length of arrays, append
# to result since it was in all of the arrays

# Execute
def intersection(arrays):
    values = {}
    result = []
    for array in arrays:
        for int in array:
            if int in values:
                values[int] += 1
                if values[int] == len(arrays):
                    result.append(int)
            else:
                values[int] = 1

    return result

# Reflection
# tests passing so meets MVP


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
