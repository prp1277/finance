import requests
import pandas as pd

AV_Key = '7FSGISSCM7BRW0N9'
SYMBOL = 'MSFT'
AV_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + SYMBOL +'&outputsize=full&apikey=' + AV_Key

pretty_print = requests.get(AV_url).json()

df1 = pd.read_json(pretty_print)
