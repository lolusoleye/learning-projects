rates = {
    "USD": 1.0,
    "GBP": 0.79,
    "EUR": 0.92,
    "BTC": 0.000015
}

uinput = float(input("how much money do you have?"))
prev = input("What is your currency")
curr = input("What do you want to convert to") 
print(uinput * (rates[curr]/rates[prev]))
