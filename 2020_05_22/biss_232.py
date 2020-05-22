class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []  # for pop and top 
        self.s2 = []  # for push

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s2.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s1:
            return self.s1.pop()
        else:
            while self.s2:
                self.s1.append(self.s2.pop())
            return self.s1.pop()
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s1:
            return self.s1[-1]
        else:
            while self.s2:
                self.s1.append(self.s2.pop())
            return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == len(self.s2) == 0