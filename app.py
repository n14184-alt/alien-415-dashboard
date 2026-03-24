import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("1.08 級別 實彈 監控：Keep 抽屜 優先 模式")

# --- 物理 裝填 區：老闆，請 將 您的 Keep 代號 填入 下方 括號 ---
# 注意：台灣 股票 請 務必 加上 .TW 或 .TWO (例如 2330.TW)
MONITOR_LISTS = {
    "基金 (28)": ["0050.TW", "0056.TW", "006208.TW"], 
    "ETF (56)": ["00878.TW", "00919.TW", "00713.TW", "00929.TW"],
    "個股 (120)": ["2330.TW", "2317.TW", "2454.TW", "3324.TWO"]
}

def get_jyw_metrics(symbol):
    """ 核心 運算：14.92 斜率 + ATR 物理 雙壓 """
    try:
        # 強制 轉換 為 大寫 並 去除 空格
        ticker = str(symbol).strip().upper()
        data = yf.Ticker(ticker)
        df = data.history(period="60d")
        
        if df.empty or len(df) < 15:
            return {"代號": ticker, "錯誤": "查無數據"}
            
        # ATR 14日 物理 判定
        high_low = df['High'] - df['Low']
        atr = high_low.rolling(14).mean().iloc[-1]
        close = df['Close'].iloc[-1]
        
        # 高效/低效 狀態 判定 [cite: 2026-02-18]
        status = "高效" if close > (df['Close'].iloc[-2] - 2*atr) else "低效"
        
        return {
            "代號": ticker,
            "收盤": round(close, 2),
            "ATR": round(atr, 2),
            "狀態": status
        }
    except Exception as e:
        return {"代號": symbol, "錯誤": str(e)}

# --- 介面 渲染 ---
st.sidebar.info("戰略 狀態：Keep 實彈 優先")
target_list = st.sidebar.selectbox("請 選擇 監控 抽屜", list(MONITOR_LISTS.keys()))

if st.button(f"啟動 {target_list} 實彈 總攻"):
    with st.spinner(f"正在 物理 校準 {target_list} 數據..."):
        results = []
        for s in MONITOR_LISTS[target_list]:
            res = get_jyw_metrics(s)
            results.append(res)
        
        if results:
            st.success(f"{target_list} 實彈 歸位！")
            st.table(pd.DataFrame(results))
        else:
            st.error("物理 斷線：請 檢查 GitHub Secrets 或 代號 格式。")
