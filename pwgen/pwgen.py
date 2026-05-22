import string 
import random


length = int(input("Input the length of your password:"))
numq = input("Do you want numbers?  (Y/N)  ")
symq= input("Do you want symbols?  (Y/N)  ")
pool = string.ascii_letters

digits = string.digits         # 0-9
punctuation = string.punctuation    # !@#$%^&* etc


if numq == "Y":
    pool = pool + digits  
if symq == "Y":
    pool = pool + punctuation

pw = ""
for i in range(length):
    pw = pw + (random.choice(pool))


print(pw)
