
str1 = 'abcabbcabac'
'''
h - 1
e - 1
l - 2
o - 1
'''
'''
# get count of each character
di = {}
for char in str1:
    if char not in di.keys():
        di[char] = 1
    else:
        di[char] += 1
print("Final char count : ", di)
'''

def get_charcount(st):
    di = {}
    for char in str1:
        if char not in di.keys():
            di[char] = 1
        else:
            di[char] += 1
    # print("Final char count : ", di)
    return di

ch_count = get_charcount(str1)
print("Final char count : ", ch_count)


print(10)

x = 10
print("Value of x: ", x)

def get_charcount(st):
    di = {}
    for char in str1:
        if char not in di.keys():
            di[char] = 1
        else:
            di[char] += 1
    print("Final char count : ", di)

get_charcount(str1)





