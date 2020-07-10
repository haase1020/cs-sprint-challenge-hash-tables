# understand and plan:
# three parameters: weight limit "limit", item weights "weights", "length" of list
# find sum of two items i and i2 = limit
# return tuple in order of i, i2
# if no pair exists, return None
# use dictionary my_dict= {} to run in linear time

# execute
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    my_dict = {}
    for i in range(length):
        if limit - weights[i] in my_dict:
            key = limit - weights[i]
            i2 = my_dict[key]
            print('i', i)
            print('i2', i2)
            return [i, i2]
        my_dict[weights[i]] = i
        print('my_dict', my_dict)

    return None


weights = [4, 6, 10, 15, 16]
get_indices_of_item_weights(weights, 5, 21)


# reflect: passing tests so meets MVP for problem
