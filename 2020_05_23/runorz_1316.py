class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = list()
        for i in range(2, len(text)+1, 2):
            for j in range(len(text)):
                if j + i > len(text):
                    break
                if text[j:int((i+j+j)/2)] == text[int((i+j+j)/2):j+i]:
                    if not text[j:int((i+j+j)/2)] in res:
                        res.append(text[j:int((i+j+j)/2)])
        return len(res)
