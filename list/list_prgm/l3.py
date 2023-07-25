def all_permutations(lst):
    if len(lst) <= 1:
        pass
        return [lst]
    
    result = []
    # print(result)
    for i in range(len(lst)):
        first_element = lst[i]
        remaining_elements = lst[:i] + lst[i+1:]
        # print(remaining_elements)
        permutations_of_remaining = all_permutations(remaining_elements)
        
        for perm in permutations_of_remaining:
            print()
            print([first_element]+perm)
            result.append([first_element] + perm)
    
    return result

# Test the function
my_list = [1, 2, 3]
result = all_permutations(my_list)
print(result)