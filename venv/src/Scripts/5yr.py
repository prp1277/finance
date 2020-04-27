#%%
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#%%
msft = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/MSFT-5Yr.csv")
chwy = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/CHWY-5Yr.csv")
hal = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/HAL-5Yr.csv")
spce = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/SPCE-5Yr.csv")
spot = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/SPOT-5Yr.csv")
twtr = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/TWTR-5Yr.csv")
wmt = pd.read_csv("/home/prp1277/Github-Repos/datasets/data/csv/Fidelity/WMT-5Yr.csv")
#%%
msft["ticker"] = "MSFT"
chwy["ticker"] = "CHWY"
hal["ticker"] = "HAL"
spce["ticker"] = "SPCE"
spot["ticker"] = "SPOT"
twtr["ticker"] = "TWTR"
wmt["ticker"] = "WMT"
#%%
cols = [
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "vma(close)",
    "LR",
    "BB(Upper)",
    "BB(Lower)",
    "SD(Population)",
    "ticker",
]
msft.columns = cols
chwy.columns = cols
hal.columns = cols
spce.columns = cols
spot.columns = cols
twtr.columns = cols
wmt.columns = cols
#%%
newdf = msft.append(twtr, ignore_index=True)
newdf = newdf.append(wmt, ignore_index=True)
newdf = newdf.append(hal, ignore_index=True)
newdf = newdf.append(spce, ignore_index=True)
newdf = newdf.append(spot, ignore_index=True)
newdf = newdf.append(chwy, ignore_index=True)
#%%
new_fig = px.line(newdf, x=newdf["date"], y=newdf["open"], color=newdf["ticker"])
new_fig.update_layout(template="ggplot2")
new_fig.show()


# %%
