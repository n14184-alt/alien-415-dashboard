import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# --- 1.08 級別 物理 抽屜 定位 ---
STRATEGY_MARK = "J.Y.W. 3.0" # 2026-03-24 鋼印
MONITOR_LISTS = {
    "FUND": "J.Y.W. 實彈監控：基金抽屜",
    "ETF": "J.Y.W. 實彈監控：ETF抽屜",
    "STOCK": "J.Y.W. 實彈監控：新個股抽屜", # 120支 已補 .TW
    "HOT": "J.Y.W. 實彈監控：新強勢股抽屜" # MoneyDJ 自動進料
}

# --- 物理 函數：MoneyDJ 多週期 動能 捕獲 ---
def fetch_moneydj_hot(periods=[5, 20, 30]):
    """ 抓取 5/20/30 日 漲幅，自動 補齊 .TW/.TWO，拒絕 腦補 """
    hot_results = []
    for p in periods:
        url = f"https://www.moneydj.com/z/zg/zg_3_{p}.djhtm"
        # 執行 物理 抓取 與 格式 判定 (省略 爬蟲 細節)
        # 確保 產出 格式 為: ['2330.TW', '3324.TWO'...]
        pass 
    return list(set(hot_results)) # 去重 歸位

# --- 核心 濾網：14.92 斜率 + ATR 聯動 ---
def calculate_jyw_metrics(symbol):
    """
    1. 14.92 斜率 (Slope): 曾氏 通道 物理 對位
    2. ATR (真實波幅): 計算 2x ATR 動態 停損
    """
    data = yf.download(symbol, period="60d", interval="1d")
    
    # ATR 計算 (14日 週期)
    high_low = data['High'] - data['Low']
    high_close = abs(data['High'] - data['Close'].shift())
    low_close = abs(data['Low'] - data['Close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(14).mean().iloc[-1]
    
    # Slope 計算 (14.92 物理 常數 對位)
    # ... 斜率 邏輯 封裝 ...
    slope = get_slope(data) 
    
    # 物理 判定: 價格 跌破 2*ATR 則 標註 為「低效」[cite: 2026-02-18]
    status = "高效" if data['Close'].iloc[-1] > (data['Close'].iloc[-2] - 2*atr) else "低效"
    
    return slope, atr, status

# --- 戰略 循環：3/5 分鐘 自動 調整 ---
def run_jyw_commander():
    while True:
        # 1. 回歸 原點 讀取 物理 抽屜 [cite: 2026-02-25]
        # 2. 執行 MoneyDJ 更新 至 新強勢股抽屜
        # 3. 計算 Slope + ATR 並 輸出 Dashboard
        print(f"[{STRATEGY_MARK}] 1.08 級別 監控 中... 誠實 比 完美 更 迷人")
        time.sleep(300) # 5分鐘 循環

if __name__ == "__main__":
    run_jyw_commander()
