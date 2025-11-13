def nth(arr, n = 0):
    """
    Gets the element at index n of list. If n is negative, the nth element from the end is returned.

    Args:
        arr (list): The list to query.
        n (int): The index of the element to return.

    Returns:
        (Any): Returns the nth element of list.
    """

    if n > len(arr) - 1 or abs(n) > len(arr):
        return None
        
    return arr[n]

# For testing
# array = ['a', 'b', 'c', 'd']
# print(nth(array, 1)) # 'b'
# print(nth(array, -2)) # 'c'
# print(nth(array, -4)) # 'a'
# print(nth(array, -5)) # None