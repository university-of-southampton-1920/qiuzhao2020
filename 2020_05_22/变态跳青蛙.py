# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1:
            return 1
        if number%2 == 0:
            temp = self.jumpFloorII(number/2)
            return temp*temp*2
        if number%2 == 1:
            temp = self.jumpFloorII(number-1)
            return temp*2
			
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <= 0:
            return 0
        else:
            return pow(2,number-1)