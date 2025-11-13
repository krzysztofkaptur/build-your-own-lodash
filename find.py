def find(collection, predicate):
    """
    Iterates over elements of collection, returning the first element predicate returns truthy for. The predicate is invoked with three arguments: (value, index|key, collection).

    Args:
        collection (list or dict): The collection to inspect.
        predicate (function): The function invoked per iteration.
        fromIndex (int, optional): The index to search from. Defaults to 0.

    Returns:
        (Any): Returns the matched element, else None.
    """
    result = None

    for item in collection:
        if predicate(item):
            result = item
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

# print(find(users, test1)) # dict for 'barney'

# def test2(o):
#     return o["age"] == 1 and o["active"] == True

# print(find(users, test2)) # dict for 'pebbles'

# def test3(o):
#     return o["active"] == False

# print(find(users, test3)) # dict for 'fred'