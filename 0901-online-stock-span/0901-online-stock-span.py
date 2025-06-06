class StockSpanner:

    def __init__(self):
        self.st=[]
        self.lst=[]

    def next(self, price: int) -> int:
        if self.st==[]:
            self.st.append(price)
            self.lst.append(1)
            return 1
        ct=1
        while self.st:
            if self.st[-1]<=price:
                ct+=self.lst.pop()
                self.st.pop()
            else:
                break
        self.st.append(price)
        self.lst.append(ct)
        return ct


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)