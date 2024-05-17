"""
1. Two pointer approach
2. Map Method
"""

import copy

def two_sum(nums, target):
    temp_dict = {}
    for i, item in enumerate(nums):
        temp_dict[target - item] = i
    print(temp_dict)
    
    for i, item in enumerate(nums):
        if temp_dict.get(item) is not None:
            return [i, temp_dict.get(item)]

if __name__ == "__main__":
    nums = [3, 3]
    target = 6

    res = two_sum(nums, target)
    print(res)

l = [1,2,4]

copy.deepcopy(l)