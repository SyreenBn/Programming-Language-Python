def is_element_of(user_element, user_set):
    A = set(user_element)
    B = set(user_set)
    if A in B:
        return True
    else:
        return False
    
def is_subset_of (user_small_set, user_set):
    A = set(user_small_set)
    B = set(user_set)
    if A.issubset(B):
        return True
    else:
        return False

user_input = input("Please, enter a set relationship query: ")
div = user_input.split()
if div[1].upper() == 'IN':
    print(is_element_of(div[0], div[2]))
    
elif div[1].upper() == 'SUBSET':
    print(is_subset_of (div[0], div[2]))

else:
    print ("Your operation is out of range")
