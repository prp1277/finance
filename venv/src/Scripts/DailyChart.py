# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

msft_04032020 = "/home/prp1277/Github-Repos/finance/venv/src/data/msft_04032020.csv"
msft_df = pd.read_csv(msft_04032020)

msft_df["Timestamp"] = pd.to_datetime(msft_df["Date"] + "T" + msft_df["Time"])
msft_df

# %%
fig = px.scatter(msft_df, x="Timestamp", y="Close", title="Microsoft")
fig.update_xaxes(rangeslider_visible=True)
fig.show()

# %%
dt_min = min(msft_df["Timestamp"])
print(dt_min)
dt_max = max(msft_df["Timestamp"])
print(dt_max)

# %%
candlestick = go.Figure(
    data=[
        go.Candlestick(
            x=msft_df["Timestamp"],
            open=msft_df["Open"],
            close=msft_df["Close"],
            high=msft_df["High"],
            low=msft_df["Low"],
        )
    ]
)

candlestick.update_layout(
    xaxis_range=[dt_min, dt_max], title_text="Microsoft", autosize=True,
)

candlestick.update_xaxes(
    rangeselector=dict(
        buttons=list(
            [
                dict(count=1, label="1 Day", step="day", stepmode="backward"),
                dict(count=2, label="2 Day", step="day", stepmode="backward"),
            ]
        )
    )
)

candlestick.show()
