def difference(arr1, arr2):
    """
    Creates an list of list values not included in the other given lists. The order and references of result values are determined by the first list.

    Args:
        arr1 (list): List of items to be checked.
        arr2 (list): List of items to be checked against.

    Returns:
        list: A new list with unique items from arr1.
    """
        
    result = []

    for item in arr1:
        if item not in arr2:
            result.append(item)

    return result

# For testing
# print(difference([2, 1], [2, 3])) # [1]