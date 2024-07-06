# Problem: Find the First Occurrence of a Target in a Sorted Array
# Description:
# Given a sorted array of integers arr and an 
# integer target, write a function to find the first occurrence 
# of target in arr. If target is not present in arr, return -1.

# input - arr, target int
# goal - find first occurence of target int
# output - index of target's first occurence, if not found result = -1

def binary_first(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1 # to store index of first occurence (-1 is starting output if target absent)

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid # reassign result value to mid index
            right = mid - 1 # move to the left to find the first occurence of target
        elif arr[mid] < target: # ie arr[mid] = 5, target = 9, then move left pointer up to adjust new mid index
            left = mid + 1
        else:
            right = mid - 1

        
    return result 

arr = [1,2,2,2,3,4,5,5,6,8]
target = 5
print(binary_first(arr, target)) # Output is 6