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
    "ETF (56)": ["00913.TW", "00830.TW", "00899.TW", "00733.TW", "00891.TW", "0061.TW", "00660.TW", "00918.TW", "00991A.TW", "00885.TW", "00940.TW", "00988A.TW", "00892.TW", "00960.TW", "00652.TW", "0056.TW", "00642U.TW", "00965.TW", "00878.TW", "0052.TW", "00894.TW", "00713.TW", "00981A.TW", "00909.TW", "00941.TW", "0050.TW", "00682U.TW", "00910.TW", "00980S.TW", "00635U.TW", "00947.TWO", "00735.TW", "00919.TW", "00876.TW", "00681R.TW", "00762.TW", "00757.TW", "0051.TW", "00924.TW", "00877.TW", "00679B.TW", "006201.TWO", "00928.TWO", "00875.TW", "00954.TW", "00905.TW", "00668.TW", "00662.TW", "00646.TW", "00770.TW", "00861.TW", "00936.TWO", "00955.TW", "00963.TW", "00964.TW", "00971.TW"],
    "個股 (120)": ["2330.TW", "2891.TW", "2890.TW", "2303.TW", "2002.TW", "2885.TW", "2882.TW", "2881.TW", "1303.TW", "1216.TW", "1301.TW", "2412.TW", "3711.TW", "2344.TW", "3231.TW", "2382.TW", "2308.TW", "2301.TW", "4904.TW", "2327.TW", "2454.TW", "6505.TW", "2408.TW", "2603.TW", "2449.TW", "2357.TW", "2345.TW", "2395.TW", "2360.TW", "2368.TW", "3017.TW", "2383.TW", "6669.TW", "3008.TW", "3653.TW", "3661.TW", "7769.TW", "2059.TW", "1326.TW", "1605.TW", "1402.TW", "2610.TW", "2353.TW", "2618.TW", "2356.TW", "9904.TW", "2027.TW", "4938.TW", "2105.TW", "2609.TW", "9945.TW", "5871.TW", "3702.TW", "2615.TW", "1504.TW", "2542.TW", "2347.TW", "3037.TW", "2313.TW", "2354.TW", "1229.TW", "3706.TW", "3036.TW", "6239.TW", "2377.TW", "2915.TW", "2385.TW", "3034.TW", "2376.TW", "2912.TW", "2379.TW", "2474.TW", "2006.TW", "6176.TW", "3044.TW", "9910.TW", "3005.TW", "1513.TW", "1319.TW", "6285.TW", "6415.TW", "3189.TW", "2539.TW", "2049.TW", "6446.TW", "6191.TW", "1503.TW", "1477.TW", "3023.TW", "8046.TW", "2451.TW", "1476.TW", "3665.TW", "5434.TW", "8464.TW", "2404.TW", "6139.TW", "2258.TW", "1519.TW", "1590.TW", "1795.TW", "2645.TW", "6531.TW", "6789.TW", "3533.TW", "8454.TW", "3443.TW", "8996.TW", "6409.TW", "6472.TW", "8210.TW", "7799.TW", "6442.TW", "6805.TW", "6890.TW", "6526.TW", "7750.TW", "5269.TW", "6781.TW", "6515.TW", "4583.TW"]
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
