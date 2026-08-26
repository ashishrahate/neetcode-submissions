class MedianFinder:

    def __init__(self):
        self.arr = []

        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

        

    def findMedian(self) -> float:
        self.arr.sort()
        n = len(self.arr)
        mid = 0
        if n%2:
            mid = float(self.arr[n//2]) # 5 //2 -> 2 
        else:
            mid = (self.arr[n //2] + self.arr[(n//2) - 1])/2.0 # 4 // 2  0 1 2 3
        return mid
        
        