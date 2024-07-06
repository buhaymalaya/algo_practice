# Problem: Binary Search for the Presence of a Target Number

# Given a sorted list of integers, 
# write a function to determine if a target number 
# exists in the list using binary search. If the target number is found, 
# return True. If it is not found, return False.

# input: arr of int, an int
# output: boolean
# binary search

def binary_bool(arr, target):
    left = 0 # assign index value to left
    right = len(arr) - 1 # assign index value of last element to right

    while left <= right: # constraint
        mid = (left + right) // 2 # mid will be basis of search

        if arr[mid] == target:
            return True # bc we have found it
        elif arr[mid] < target:
            left = mid + 1 # since sorted arr, we start at left side
        else:
            right = mid - 1 # we 

    return False # if not found using binary search to iterate through list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
target = 9
print(binary_bool(arr, target))