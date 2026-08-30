class MedianFinder:

    def __init__(self):
        self.data = []
        

    def addNum(self, num: int) -> None:
        self.data.append(num)
        

    def findMedian(self) -> float:
        self.data.sort()
        
        if len(self.data) & 1:
            return self.data[len(self.data) // 2]
        else:
            return (self.data[len(self.data) // 2] + self.data[len(self.data) // 2 - 1]) / 2
        
        