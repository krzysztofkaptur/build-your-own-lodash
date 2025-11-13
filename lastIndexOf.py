def lastIndexOf(arr, value, fromIndex = None):
    """
    Gets the index at which the first occurrence of value is found in list except that it iterates over elements of list from right to left.

    Args:
        arr (list): The list to inspect.
        value (any): The value to search for.
        fromIndex (int, optional): The index to search from. Defaults to 0.

    Returns:
        (Any): Returns the last element of list.
    """
        
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