"""
Name: byroncbr_219.py
Author: bangrenc
Time: 5/3/2020 9:41 AM
"""

def containsNearbyDuplicate(nums, k):
    record = {}

    for i, num in enumerate(nums): #查表法
        if nums[i] in record:
            return True

        record[num] = i

        if len(record) == k+1: #设置了窗口的大小
            record.pop(nums[i-k])

    return False

if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    result = containsNearbyDuplicate(nums, k)
    print(result)









