"""
Name: byroncbr_03.py
Author: bangrenc
Time: 2/3/2020 10:35 PM
"""

from collections import Counter

def collect_nums(nums):
    count = Counter(nums)
    for i, num in enumerate(count):
        if count[num] > 1:
            return num

if __name__ == '__main__':
    nums = [2, 3, 1, 0, 2, 5, 3]
    collect_result = collect_nums(nums)
    print(collect_result)



