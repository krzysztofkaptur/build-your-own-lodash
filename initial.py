def initial(arr):
    """
    Gets all but the last element of list.

    Args:
        arr (list): The list to query.

    Returns:
        (list): Returns the slice of list.
    """
        
    return arr[:len(arr) - 1]

# For testing
# print(initial([1,2,3])) # [1,2]