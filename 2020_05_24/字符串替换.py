# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        i = 0
        while(i<len(s)):
            if s[i] == ' ':
                if i+1>(len(s)-1):
                    s = s[:i] + '%20'
                    i += 2
                else:
                    s = s[:i] + '%20' + s[i+1:]
                    i += 2
            else:
                i += 1
        return s