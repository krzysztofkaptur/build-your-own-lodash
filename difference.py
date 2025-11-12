# Creates an array of array values not included in the other given arrays. The order and references of result values are determined by the first array.
def difference(arr1, arr2):
    result = []

    for item in arr1:
        if item not in arr2:
            result.append(item)

    return result

# For testing
# print(difference([2, 1], [2, 3])) # [1]