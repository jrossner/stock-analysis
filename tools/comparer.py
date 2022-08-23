class CompareStocks():
    def __init__(self,symbol1,symbol2):
        self.stock1 = symbol1
        self.stock2 = symbol2
        
    #@classmethod
    def marketVal(self):
        s1mc = yf.Ticker(self.stock1).info["marketCap"]
        s2mc = yf.Ticker(self.stock2).info["marketCap"]

        if s1mc > s2mc:
            mcDiff = "{:,}".format(s1mc-s2mc)
            mcRatio = "{:,}".format(round(s1mc/s2mc,2))
            print(f"{self.stock1} is valued at ${mcDiff} more than {self.stock2}.")
            print(f"{self.stock1} is valued {mcRatio} times more than {self.stock2}.")
        else:
            pDiff = "{:,}".format(s2mc-s1mc)
            mcRatio = "{:,}".format(round(s2mc/s1mc,2))
            print(f"{self.stock2} is valued at ${mcDiff} more than {self.stock1}.")
            print(f"{self.stock2} is valued {mcRatio} times more than {self.stock1}.")
            

cs = CompareStocks("AAPL","ABML")
cs.marketVal()
