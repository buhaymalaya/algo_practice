# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# example
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# locate the two values within the arr that equals to target value
# output is a list of the two indices of said values; output = [].append
# iterate through the arr to find values 
# range loop to find the indeces
# use a condition that ensures the iterated value is <= target, if > target then dont add to running sum
# what if running sum > target 

# Input: nums = [11, 2, 15, 8, 7], target = 9
# if running sum > target return false
# for index, value loop

# nums[2]

def target(arr, tar):
    output = []
    running_sum = 0
    for i in range(len(arr)):
        if arr[i] <= tar:
            # print(arr[i])
            running_sum += arr[i]
            output.append(i)
    print(running_sum)

print(target([11, 2, 15, 8, 7], 9))


# consider - two pointers binary search
# running value
# value = tar - current iterated value
# 