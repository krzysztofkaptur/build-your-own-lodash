def compact(arr):
    """
    Creates an list with all falsey values removed. The values false, None, 0, "", and NaN are falsey.

    Args:
        arr (list): List of items.

    Returns:
        list: A new list with falsey values removed.
    """
        
    result = []

    for item in arr:
        if bool(item):
            result.append(item)

    return result

# For testing
# print(compact([0, 1, False, 2, '', 3])) # [1, 2, 3]