# logic/strategy_runner.py

import pandas as pd
from rsi_strategy import calculate_rsi, get_rsi_signal

def run_rsi_strategy(etf_code: str, prices: pd.Series):
    print(f"▶️ [전략 실행] ETF 코드: {etf_code}")

    # RSI 계산
    rsi_series = calculate_rsi(prices)
    rsi_value = round(rsi_series.iloc[-1], 2)
    signal = get_rsi_signal(rsi_series)

    # 결과 출력
    print(f"📈 최신 RSI: {rsi_value}")
    print(f"📌 매매 시그널: {signal}")

    return signal
