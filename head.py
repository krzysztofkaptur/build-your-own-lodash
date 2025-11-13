def head(arr):
    """
    Gets the first element of array.

    Args:
        arr (list): The array to query.

    Returns:
        (any): Returns the first element of array.
    """
    
    return arr[0] if len(arr) > 0 else None

# For tests
# print(head([1,2,3])) # 1
# print(head([])) # None