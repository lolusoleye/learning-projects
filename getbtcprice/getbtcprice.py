import requests
response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
data = response.json()
price = (data["bitcoin"])
print(f"Bitcoin price is : ${price["usd"]} ")