
# understand and plan:
# separate files at '/'. Pop() removes and returns last value from given path
# loop through queries; if query in values, then see if path in values for the query
# if exists, append to result (append takes a single argument "path")
# return result as list

# Execute
def finder(files, queries):
    values = {}
    result = []

    for path in files:
        file = path.split('/').pop()
        if file in values:
            values[file].append(path)

        else:
            values[file] = [path]
    for query in queries:
        if query in values:
            for path in values[query]:
                result.append(path)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/bin/su'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))


# Reflect:
# tests are passing so problem successfully completed
