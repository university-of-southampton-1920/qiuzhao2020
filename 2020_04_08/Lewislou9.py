class Solution:
    def isNumber(self, s: str) -> bool:
        nums = s.strip().split('e')
        if len(nums) > 2:
            return False
        for (idx, n) in enumerate(nums):
            minuses, pluses, periods = n.count('-'), n.count('+'), n.count('.')
            if not n or minuses > 1 or (n[0] != '-' and minuses == 1):
                return False
            if pluses > 1 or (n[0] != '+' and pluses == 1):
                return False
            if periods > 1 or (idx == 1 and periods):
                return False
            if len(re.findall(r'[^\+\-\.0-9]', n)) or not len(re.findall(r'\d', n)):
                return False
            
        return True