class CompareStocks():
    def __init__(self,symbol1,symbol2):
        self.stock1 = yf.Ticker(symbol1)
        self.stock2 = yf.Ticker(symbol2)
        self.name1 = self.stock1.info["shortName"]
        self.name2 = self.stock2.info["shortName"]
        
    def marketVal(self):
        s1mc = self.stock1.info["marketCap"]
        s2mc = self.stock2.info["marketCap"]

        if s1mc > s2mc:
            mcDiff = "{:,}".format(s1mc-s2mc)
            mcRatio = "{:,}".format(round(s1mc/s2mc,2))
            return f"{self.name1} is valued at ${mcDiff} more than {self.name2}.\n{self.name1} is valued {mcRatio} times more than {self.name2}."
        else:
            mcDiff = "{:,}".format(s2mc-s1mc)
            mcRatio = "{:,}".format(round(s2mc/s1mc,2))
            return f"{self.name2} is valued at ${mcDiff} more than {self.name1}.\n{self.name2} is valued {mcRatio} times more than {self.name1}."

    def recs(self):
        s1rec = self.stock1.info["recommendationKey"]
        s2rec = self.stock2.info["recommendationKey"]
        return f"{self.name1} is recommended as a {s1rec}.\n{self.name2} is recommended as a {s2rec}.\nDo your own research too."
            

## Example Use Cases
cs = CompareStocks("AAPL","FB")
cs.marketVal()
# Apple Inc. is valued at $2,249,216,950,272 more than Meta Platforms, Inc..
# Apple Inc. is valued 6.07 times more than Meta Platforms, Inc..
cs.recs()
# Apple Inc. is recommended as a buy.
# Meta Platforms, Inc. is recommended as a buy.
# Do your own research too.
