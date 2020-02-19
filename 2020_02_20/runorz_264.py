class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p = [0, 0, 0]
        factor = [2, 3, 5]
        ugly_numbers = [1]
        
        while(len(ugly_numbers) < n):
            temp = list()
            for i in range(len(p)):
                temp.append(factor[i]*ugly_numbers[p[i]])
            min_index = temp.index(min(temp))
            p[min_index] = p[min_index] + 1
            if min(temp) in ugly_numbers:
                continue
            ugly_numbers.append(min(temp))
            
        return ugly_numbers[-1]
