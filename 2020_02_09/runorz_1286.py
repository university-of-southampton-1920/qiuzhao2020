class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.index = [i for i in range(combinationLength)]
        self.characters = characters
        self.combinationLength = combinationLength

    def next(self) -> str:
        if self.hasNext() == False:
            return []
        temp = ''
        for i in self.index:
            temp += self.characters[i]
        self.index_add_one(self.combinationLength-1);
        return temp

    def hasNext(self) -> bool:
        if self.index[-1] > len(self.characters)-1:
            return False
        else:
            return True

    def index_add_one(self, last):
        self.index[last] = self.index[last] + 1
        if last == 0:
            return self.index[last] + 1
        if self.index[last] > len(self.characters)+last-len(self.index) :
            self.index[last] = self.index_add_one(last-1)
        return self.index[last] + 1
