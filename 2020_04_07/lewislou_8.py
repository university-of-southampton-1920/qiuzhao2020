import sys
import math
class Solution:
    def myAtoi(self, str: str) -> int:
        str=str.lstrip() ##取出字符串左边的空格
        result=0
        isNegative = 0
        start=0
        if (str is None or len(str) == 0):
            return 0
        
        if(str[0] == '+' or str[0] == '-'):
            start +=1
        
        if(str[0] is '-'):
            isNegative= 1
        for i in range(start, len(str)):
            if(str[i] <'0' or str[i] > '9'):
                break
            digit=int(str[i]) 
            result=result*10+ digit
        print(isNegative)
        if(isNegative):
            result=-result
        print(math.pow(-2,31))
        if result>int(math.pow(2,31)-1):
            return int(math.pow(2,31)-1)
        if result<int(math.pow(-2,31)):
            return int(math.pow(-2,31))
        return result
                