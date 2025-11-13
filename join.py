def join(arr, separator = ","):
    """
    Converts all elements in list into a string separated by separator.

    Args:
        arr (list): The list to convert.
        separator: (string, optional): The element separator. Defaults to ','.

    Returns:
        (string): Returns the joined string.
    """

    return f"{separator}".join(arr)

# For testing
# print(join(['a', 'b', 'c'], '~')) # 'a~b~c'