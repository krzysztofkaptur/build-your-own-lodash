def findIndex(arr, predicate, fromIndex = 0):
    """
    This method returns the index of the first element predicate returns truthy.

    Args:
        arr (list): The array to inspect.
        predicate (function): The function invoked per iteration.
        fromIndex (int, optional): The index to search from. Defaults to 0.

    Returns:
        (int): Returns the index of the found element, else -1.
    """
    
    result = -1

    for i in range(fromIndex, len(arr)):
        if predicate(arr[i]):
            result = i
            break
        
    return result

# For testing
# users = [
#   { 'user': 'barney',  'age': 36, 'active': True },
#   { 'user': 'fred',    'age': 40, 'active': False },
#   { 'user': 'pebbles', 'age': 1,  'active': True }
# ]

# def test1(o):
#     return o["age"] < 40

# print(findIndex(users, test1)) # 0

# def test2(o):
#     return o["age"] == 1 and o["active"] == True

# print(findIndex(users, test2)) # 2

# def test3(o):
#     return o["active"] == False

# print(findIndex(users, test3)) # 1

# def test4(o):
#     return o["age"] < 40

# print(findIndex(users, test4, 1)) # 2

# def test5(o):
#     return o["age"] < 40

# print(findIndex(users, test5, 5)) # -1