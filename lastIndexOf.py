def lastIndexOf(arr, value, fromIndex = None):
    result = None
    end = len(arr) - 1
    start = fromIndex if fromIndex is not None else end

    if fromIndex and end < fromIndex:
        return None

    for i in range(start, -1, -1):
        if arr[i] == value:
            result = i
            break

    return result

# For testing
# print(lastIndexOf([1, 2, 1, 2], 2)) # 3
# print(lastIndexOf([1, 2, 1, 2], 2, 2)) # 1