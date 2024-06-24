# Take an input n and return the sume of the numbers
# from 0 to n

def sum_range(n):
    final_sum = 0 # output
    for num in range(n+1): # range is n+1 because not inclusive
        final_sum += num # every number in range is added to output @ each iteration
    
    return final_sum # once iteration reaches last number in range (n+1), returns output

print(sum_range(5)) # 15.. 1+2+3+4+5
print(sum_range(15)) # 120.. 1+2+3+4+5+6+7+8+9+10+11+12+13+14+15
