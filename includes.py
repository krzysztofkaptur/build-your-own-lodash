def includes(collection, value):
    """
    Checks if value is in collection.

    Args:
        collection (list or dict): The collection to inspect.
        predicate (Any): The value to search for.

    Returns:
        (bool): Returns true if value is found, else false.
    """
        
    result = False

    if isinstance(collection, list):
        result = value in collection

    if isinstance(collection, dict):
        for item in collection:
            if collection[item] == value:
                result = True


    return result


# For testing
# print(includes([1, 2, 3], 1)) # True
# print(includes({ 'a': 1, 'b': 2 }, 1)) # True
# print(includes({ 'a': 1, 'b': 2 }, 3)) # False