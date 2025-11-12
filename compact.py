# Creates an array with all falsey values removed. The values false, None, 0, "", and NaN are falsey.
# compact(array)

def compact(arr):
    result = []

    for item in arr:
        if bool(item):
            result.append(item)

    return result

# For testing
# print(compact([0, 1, False, 2, '', 3])) # [1, 2, 3]