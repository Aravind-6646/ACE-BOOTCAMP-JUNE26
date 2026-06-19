from copy import deepcopy
list1 = [1, 2, 3, 4]
list2 = deepcopy(list1)
list2[2] = 100
print("Original:", list1)
print("Copy:", list2)