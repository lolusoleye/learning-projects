import requests
api = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=5&page=1")
data = api.json()

for each in data:
    print(f"The price of {each['id']} is ${each['current_price']}")
