# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# maybe find the range until number
# start at 3 and increment by 1, stop at number
# if number is divisible by 3 and 5, add it to running sum once
# sum = 0

# my solution
def solution(number):
    running_sum = 0
    for i in range(0, number, 1):
        if i % 3 == 0 and i % 5 == 0:
            running_sum += i
        elif i % 3 == 0 or i % 5 == 0:
            running_sum += i
        elif i <= 0:
            return 0
    return running_sum

print(solution(12))
print(solution(22))

# other solutions

# list comprehension

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

