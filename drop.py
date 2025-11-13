def drop(arr, num = 1):
    """
    Creates a slice of list with n elements dropped from the beginning.

    Args:
        arr (list): The list to modify.
        num (int, optional): The number of items to be removed, counting from the left. Defaults to 1

    Returns:
        list: A new list with filtered values.
    """

    if num == 0:
        return arr
    
    return arr[num:]

# For testing
# print(drop([1, 2, 3])) # [2, 3]
# print(drop([1, 2, 3], 2)) # [3]
# print(drop([1, 2, 3], 5)) # []
# print(drop([1, 2, 3], 0)) # [1, 2, 3]