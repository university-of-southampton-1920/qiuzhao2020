from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.list = [''.join(i) for i in combinations(characters,r=combinationLength)]

    def next(self) -> str:
        return self.list.pop(0)

    def hasNext(self) -> bool: