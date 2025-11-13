def reverse(arr):
    """
    Reverses list so that the first element becomes the last, the second element becomes the second to last, and so on.

    Args:
        arr (list): The array to modify.

    Returns:
        (list): Returns reversed array.
    """

    result = []

    for i in range(len(arr) - 1, -1, -1):
        result.append(arr[i])

    return result

# For testing
# print(reverse([1,2,3])) # [3,2,1]