# Currency Converter
# API: https://api.exchangerate-api.com/v4/latest/USD
# Goal: Convert a given amount in INR to USD, EUR, etc.
import requests
INR=420
api='https://api.exchangerate-api.com/v4/latest/USD'
goal=requests.get(api)

res=goal.json()

rates=res["rates"]["INR"]

USD=INR/rates
EUR=USD*res["rates"]["EUR"]
print(USD)
print(EUR)