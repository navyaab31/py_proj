# 1. update() :: update the dictionary with the elements from other dictionary
#               dict.update([other])-->None
                    
print("------------- 1. update() -----------------")
print("update the dictionary with the elements from other dictionary")


# Dictionary with three items
Dictionary1 = {'A': 'Hello', 'B': 'world', }
Dictionary2 = {'B': 'python'}
 
# Dictionary before Updation
print(Dictionary1)
 
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)

# {'A': 'Hello', 'B': 'world'}

Dictionary1 = {'A': 'hello'}
print(Dictionary1)
 
Dictionary1.update(B='hi', C='python')
print(Dictionary1)

# {'A': 'hello', 'B': 'hi', 'C': 'python'}

dict = {'m': 700, 'n':100, 't':500}
dict.update({'m':600})

# {'m': 600, 'n': 100, 't': 500}

# 2. key() :: returns list of keys in the dictionary
#               dict.keys()->list of keys
                    
print("------------- 2. key() -----------------")
print("returns list of keys in the dictionary")

Dictionary1 = {'A': 'hello', 'B': 'python', 'C': 'world'}
 
# Printing keys of dictionary
print(Dictionary1.keys())

# dict_keys(['A', 'B', 'C'])

# 3. values() :: returns list of values in the dictionary
#               dict.values()->list of keys
# The values have been stored in a reversed manner.
print("------------- 3. values() -----------------")
print("returns list of vlaues in the dictionary")

dictionary = {"raj": 2, "striver": 3, "vikram": 4}
print(dictionary.values())
# dict_values([2, 3, 4])
 
# string values
dictionary = {"geeks": "5", "for": "3", "Geeks": "5"}
print(dictionary.values())
# dict_values(['5', '3', '5'])



Dictionary1 = {'A': 'hello', 'B': 'python', 'C': 'world'}