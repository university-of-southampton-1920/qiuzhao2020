"""
Name: byroncbr_455.py
Author: bangrenc
Time: 19/3/2020 11:36 AM
"""

def findContentChildren(g, s):
    g.sort() #先从小到大排序好
    s.sort()
    print(g)
    res = 0
    i = 0
    for e in s:
        if i == len(g):
            break
        if e >= g[i]: #假如s中的一个数满足g，e和g就跳到下一个数
            res += 1
            i += 1
    return res

if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    result = findContentChildren(g, s)
    print(result)




