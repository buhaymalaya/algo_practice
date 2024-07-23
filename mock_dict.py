# Place the elements from a string into a dictionary
# where the names are the keys and the ages and letters are values
# the string example "John|23|A|Paul|20|B|Peter|30|C" must be converted into a dict

# .split() string on '|'
# create a function that iterates over list output using index
# range starts at 0, stops at length of list, steps every 3
# what if string is empty? what if it contains other special characters?

def dic(stringy):
    dicty = {}
    party = stringy.split('|')
    for i in range(0, len(party), 3):
        dicty[party[i]] = [party[i+1], party[i+2]]
    return dicty

stringy = "John|23|A|Paul|20|B|Peter|30|C"

print(dic(stringy))