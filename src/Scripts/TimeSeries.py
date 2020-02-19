import requests
import pandas as pd

AV_Key = "&apikey=7FSGISSCM7BRW0N9"
SYMBOL = "MSFT"

# Time Series
AV_Time_Series = (
    "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="
    + SYMBOL
    + "&outputsize=full"
    + AV_Key
)
Time_Series = requests.get(AV_Time_Series).json()
Time_Series_df = pd.read_json(Time_Series)

# Global Quote
AV_Global_Quote = (
    "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + SYMBOL + AV_Key
)
Global_Quote = requests.get(AV_Global_Quote).json()
Global_Quote_df = pd.read_json(Global_Quote)
