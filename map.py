def map(collection, iteratee):
    """
    Creates an list of values by running each element in collection thru iteratee.

    Args:
        collection (list): The collection to iterate over.
        predicate (function): The function invoked per iteration.

    Returns:
        (list): Returns the new mapped list.
    """
        
    result = []

    for i in range(0, len(collection)):
       result.append(iteratee(collection[i]))

    return result 

# For testing
# def square(n):
#   return n * n

# print(map([4, 8], square)) # [16, 64]
# print(map([], square)) # []
