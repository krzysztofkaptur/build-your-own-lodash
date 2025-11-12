# Creates an array with all falsey values removed. The values false, None, 0, "", and NaN are falsey.

def compact(arr):
    result = []

    for i in arr:
        if bool(i):
            result.append(i)

    return result

# For testing
print(compact([0, 1, False, 2, '', 3])) # [1, 2, 3]