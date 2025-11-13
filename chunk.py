def chunk(arr, num = 1):
    """
    Creates an list of elements split into groups the length of size. If list can't be split evenly, the final chunk will be the remaining elements.

    Args:
        arr (list): List of items.
        size (int, optional): The size of chunks. Defaults to 1.

    Returns:
        list: A new list with chunks.
    """

    result = []
    count = 0
    temp_arr = []

    for i in range(0, len(arr)):
        if count == num - 1:
            temp_arr.append(arr[i])
            result.append(temp_arr)
            count = 0
            temp_arr = []
        else:
            temp_arr.append(arr[i])
            count += 1

            if i == len(arr) - 1:
                result.append(temp_arr)
        

    return result

# For testing
# print(chunk(['a', 'b', 'c', 'd'], 2)) # [['a', 'b'], ['c', 'd']]
# print(chunk(['a', 'b', 'c', 'd'], 3)) # [['a', 'b', 'c'], ['d']]
# print(chunk(['a', 'b', 'c', 'd'], 5)) # [['a', 'b', 'c', 'd']]