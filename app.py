import streamlit as st
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# --- J.Y.W. 3.0 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 指揮部", layout="wide")
st.markdown("### 1.08 級別 實彈監控：誠實 比 完美 更 迷人")

# --- 1. MoneyDJ 抓取 函數 (5/20/30日 漲幅) ---
def get_moneydj_hot(period=30):
    url = f"https://www.moneydj.com/z/zg/zg_3_{period}.djhtm"
    try:
        # 實際 部署 時 需 加入 headers 模擬 瀏覽器
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        # 邏輯：從 table 抓取 代號 並 自動 補齊 .TW/.TWO
        # 這裡 為 邏輯 封裝，實際 需 依 MoneyDJ 網頁 結構 解析
        return ["2330.TW", "2454.TW", "1519.TW", "3324.TWO"] # 示例 輸出
    except:
        return []

# --- 2. ATR 與 Slope 核心 運算 ---
def get_jyw_metrics(symbol):
    df = yf.download(symbol, period="60d", progress=False)
    if df.empty: return None
    
    # ATR 計算
    high_low = df['High'] - df['Low']
    tr = high_low.rolling(14).mean().iloc[-1] # 簡化 TR 計算
    
    # 14.92 斜率 邏輯
    # (此處 封裝 老闆 的 曾氏 通道 物理 公式)
    slope = 14.92 # 示例 值
    
    # 物理 判定 [cite: 2026-02-18]
    status = "高效" if df['Close'].iloc[-1] > (df['Close'].iloc[-2] - 2*tr) else "低效"
    return {"Slope": slope, "ATR": tr, "Status": status}

# --- 3. Streamlit 介面 渲染 ---
def main():
    st.sidebar.title("J.Y.W. 3.0 抽屜")
    mode = st.sidebar.selectbox("切換 週期", [5, 20, 30])
    
    if st.button("啟動 MoneyDJ 實彈 掃描"):
        hot_stocks = get_moneydj_hot(mode)
        st.write(f"已 捕獲 {len(hot_stocks)} 支 強勢 實彈...")
        
        results = []
        for s in hot_stocks:
            m = get_jyw_metrics(s)
            if m: results.append({"代號": s, **m})
        
        st.table(pd.DataFrame(results))

if __name__ == "__main__":
    main()
