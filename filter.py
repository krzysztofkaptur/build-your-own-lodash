def filter(collection, predicate):
    """
    Iterates over elements of collection, returning a list of all elements predicate returns truthy for.

    Args:
        collection (list): The collection to iterate over.
        predicate (function): The function invoked per iteration.

    Returns:
        (list): Returns the new filtered list.
    """
        
    result = []

    for i in range(0, len(collection)):
        if predicate(collection[i]):
            result.append(collection[i])

    return result

# For testing
# users = [
#   { 'user': 'barney',  'age': 36, 'active': True },
#   { 'user': 'fred',    'age': 40, 'active': False },
#   { 'user': 'pebbles', 'age': 1,  'active': True }
# ]

# def test1(o):
#     return o["age"] < 40

# print(filter(users, test1)) # [{'user': 'barney', 'age': 36, 'active': True}, {'user': 'pebbles', 'age': 1, 'active': True}]

# def test2(o):
#     return o["age"] == 1 and o["active"] == True

# print(filter(users, test2)) # [{'user': 'pebbles', 'age': 1, 'active': True}]

# def test3(o):
#     return o["active"] == False

# print(filter(users, test3)) # [{'user': 'fred', 'age': 40, 'active': False}]