import pandas as pd
import yfinance as yf

# variables for modeling
variable_list = ["ebitdaMargins","profitMargins","grossMargins","operatingCashflow","revenueGrowth",
"operatingMargins","recommendationKey","freeCashflow","earningsGrowth","targetMeanPrice","targetMedianPrice",
"totalRevenue","forwardPE","pegRatio","shortPercentOfFloat","heldPercentInsiders","priceToBook","forwardEps"]

# get all tickers from S&P 500
sp500 = pd.read_csv("tickers.csv",sep=',')

# format stock tickers (like BRK.B) to yahoo format
sp500["Symbol"] = sp500["Symbol"].str.replace(".","/")

# start our data frame
data = pd.DataFrame(index = sp500["Symbol"])

# set up data frame with variables
for var in variable_list:
    data[var] = None

# iterate through and fill dataframe with yfinance returned info
for symb in data.index:
  info = yf.Ticker(symb).info
  for key in data.columns:
      try:
          data.loc[symb][key] = info[key]
      except:
          print(f"issue with {symb}")
          break

# drop all stocks that have missing info
data = data.dropna()

# format "none" (no recommendations) to "No recommendation"
stock_data["recommendationKey"] = stock_data["recommendationKey"].str.replace("none","No recommendation")

# output data frame as json file
data.to_json("stock_data.json")
