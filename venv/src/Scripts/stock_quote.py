import requests
import json

watchlist = ["MSFT", "NDAQ", "SPOT", "CHWY", "SPCE", "DIS"]

baseURL = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&apikey=7FSGISSCM7BRW0N9&symbol="

for x in watchlist:
    print(requests.get(baseURL + x).json())
