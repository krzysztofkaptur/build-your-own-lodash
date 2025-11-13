def fill(arr, value, start = 0, end = None):
    """
    Fills elements of list with value from start up to, but not including, end.

    Args:
        arr (list): The list to modify.
        value (Any): The value to fill elements with.
        start (int, optional): The index to start filling. Defaults to 0.
        end (int, optional): The index to finish filling. Defaults to None

    Returns:
        list: A new list with updated values.
    """
    
    result = []

    for i in range(0, len(arr)):
        if start != None and end != None:
            if i >= start and i < end:
                result.append(value)
            else:
                result.append(arr[i])
        else:
            result.append(value)



    return result

# For testing
# print(fill([1, 2, 3], 'a')) # ['a', 'a', 'a']
# print(fill([None] * 3, 2)) # [2, 2, 2]
# print(fill([4, 6, 8, 10], '*', 1, 3)) # [4, '*', '*', 10]