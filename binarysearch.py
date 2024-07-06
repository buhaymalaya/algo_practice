# Problem: Binary Search for a Target Number

# Given a sorted list of integers, 
# write a function to find a target number using binary search. 
# If the target number is found, return its index. If it is not found, return -1.

# input - array containing int
# output - index of target number if found
# return -1 if target absent
# set pointers: one for start, other for end
# increment pointer by 1 to iterate through arr


def binary_search(listy, target):
    start_pointer = 0
    end_pointer = len(listy) - 1

    while start_pointer <= end_pointer:

        mid_pointer = (start_pointer + end_pointer) // 2

        if listy[mid_pointer] == target:
            return mid_pointer
        elif listy[mid_pointer] < target:
            start_pointer = mid_pointer + 1
        else:
            start_pointer = mid_pointer - 1
        

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(binary_search(arr, target))  # Output: 4 since target 5 is at index 4

