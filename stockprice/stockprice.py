import yfinance as yf
ticker = input("Input your ticker:")
stock = yf.Ticker(ticker)
info = stock.info
curr_price = info["currentPrice"]
oprice = info["open"]
print(f"Current price{curr_price} and your open price is {oprice}.")
if curr_price > oprice:
    print(f"{ticker} is up for today")
if curr_price < oprice:
    print(f"{ticker} is down for today")
if curr_price == oprice:
    print(f"{ticker} hasn't moved from the open price.")