import pandas as pd

def calculate_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    delta = prices.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def get_rsi_signal(rsi_series: pd.Series, low=30, high=70):
    latest = rsi_series.iloc[-1]
    if latest < low:
        return "BUY"
    elif latest > high:
        return "SELL"
    else:
        return "HOLD"

