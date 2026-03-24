import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("1.08 級別 實彈 監控：Keep 抽屜 優先 模式")

# --- 核心 裝填：請 在 這裡 直接 填入 您的 實彈 代號 ---
# 老闆，我 先 幫 您 填入 幾支 指標，您可以 依照 Keep 內容 自由 增減
MONITOR_LISTS = {
    "基金 (28)": ["0050.TW", "0056.TW", "006208.TW"], 
    "ETF (56)": ["00878.TW", "00919.TW", "00713.TW", "00929.TW"],
    "個股 (120)": ["2330.TW", "2317.TW", "2454.TW", "2308.TW", "2382.TW"]
}

def get_jyw_metrics(symbol):
    """ 執行 14.92 斜率 + ATR 物理 雙壓 """
    try:
        df = yf.download(symbol, period="60d", progress=False)
        if df.empty: return None
        # ATR 運算 (14日 均值)
        atr = (df['High'] - df['Low']).rolling(14).mean().iloc[-1]
        # 物理 判定 [cite: 2026-02-18]
        status = "高效" if df['Close'].iloc[-1] > (df['Close'].iloc[-2] - 2*atr) else "低效"
        return {
            "代號": symbol,
            "收盤": round(df['Close'].iloc[-1], 2),
            "ATR": round(atr, 2),
            "狀態": status
        }
    except: return None

# --- 介面 渲染 ---
target_list = st.sidebar.selectbox("請 選擇 監控 抽屜", list(MONITOR_LISTS.keys()))

if st.button(f"啟動 {target_list} 實彈 掃描"):
    with st.spinner(f"正在 物理 讀取 {target_list}..."):
        results = [get_jyw_metrics(s) for s in MONITOR_LISTS[target_list] if get_jyw_metrics(s)]
        if results:
            st.success(f"{target_list} 實彈 掃描 完成！")
            st.table(pd.DataFrame(results))
        else:
            st.warning("數據 抓取 失敗，請 檢查 網路 或 代號 格式。")
