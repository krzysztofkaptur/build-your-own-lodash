# Creates a slice of array with n elements dropped from the beginning.
# drop(array, [n=1])

def drop(arr, num = 1):
    if num == 0:
        return arr
    
    return arr[num:]

# For testing
# print(drop([1, 2, 3])) # [2, 3]
# print(drop([1, 2, 3], 2)) # [3]
# print(drop([1, 2, 3], 5)) # []
# print(drop([1, 2, 3], 0)) # [1, 2, 3]