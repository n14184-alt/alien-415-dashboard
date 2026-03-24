import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("1.08 級別 實彈 監控：Keep 抽屜 優先 模式")

# --- 1.08 級別 中文 映射 字典 [cite: 2026-03-25] ---
STOCK_NAME_MAP = {
    "2330.TW": "台積電 ★★★",
    "2891.TW": "中信金",
    "2454.TW": "聯發科 ★★★",
    "2412.TW": "中華電",
    "2002.TW": "中鋼",
    "2308.TW": "台達電 ★★★",
    "2881.TW": "富邦金",
    "1303.TW": "南亞",
    "1216.TW": "統一",
    "4904.TW": "遠傳"
}

# --- 物理 裝填 區 ---
MONITOR_LISTS = {
    "基金 (28)": [
        "F0HKG05X22:FO", "F00000MMGD:FO", "F0HKG05WZM:FO", "F0HKG05X2C:FO", 
        "F000015CWL:FO", "F00001EBH4:FO", "F0HKG05WYP:FO", "F00000ZH5C:FO", 
        "F0HKG05WSZ:FO", "F0HKG05WZO:FO", "F00000X5LG:FO", "F00000OXXD:FO", 
        "F00001EMTX:FO", "F00001ELXG:FO", "F00001EMTU:FO", "F0GBR04ARK:FO", 
        "F000000GKS:FO", "F0GBR04V6U:FO", "F0GBR04SNN:FO", "F0HKG062PO:FO", 
        "F0GBR04AC1:FO", "F0GBR04BG3:FO", "F00000PXGY:FO", "F00001ELXE:FO", 
        "F00001ELXD:FO", "F00001ELXF:FO", "F0GBR04ASX:FO", "F00000MK1B:FO"
    ],
    "ETF (56)": [
        "00913.TW", "00830.TW", "00899.TW", "00733.TW", "00891.TW", 
        "0061.TW", "00660.TW", "00918.TW", "00991A.TW", "00885.TW", 
        "00940.TW", "00988A.TW", "00892.TW", "00960.TW", "00652.TW", 
        "0056.TW", "00642U.TW", "00965.TW", "00878.TW", "0052.TW", 
        "00894.TW", "00713.TW", "00981A.TW", "00909.TW", "00941.TW", 
        "0050.TW", "00682U.TW", "00910.TW", "009805.TW", "00635U.TW", 
        "00735.TW", "00919.TW", "00876.TW", "00681R.TW", "00762.TW", 
        "00757.TW", "0051.TW", "00924.TW", "006201.TWO", "00928.TWO", 
        "00875.TW", "00954.TW", "00905.TW", "00668.TW", "00662.TW", 
        "00646.TW", "00770.TW", "00861.TW", "00963.TW", "00964.TW", "00971.TW"
    ],
    "個股 (精選)": list(STOCK_NAME_MAP.keys())
}

def get_jyw_metrics(symbol):
    """ 核心 運算：名稱 映射 + 狀態 判定 """
    try:
        ticker = str(symbol).strip().upper()
        display_name = STOCK_NAME_MAP.get(ticker, ticker)
        
        data = yf.Ticker(ticker)
        df = data.history(period="60d")
        
        if df.empty or len(df) < 15:
            return {"名稱": display_name, "錯誤": "查無數據", "狀態": "未知", "ATR": 0}
            
        high_low = df['High'] - df['Low']
        atr = high_low.rolling(14).mean().iloc[-1]
        close = df['Close'].iloc[-1]
        
        # 狀態 判定：替換「低壓」為「低效」 [cite: 2026-02-18]
        status = "高效" if close > (df['Close'].iloc[-2] - 2*atr) else "低效"
        
        return {
            "名稱": display_name,
            "收盤": round(close, 2),
            "ATR": round(atr, 2),
            "狀態": status
        }
    except Exception as e:
        return {"名稱": symbol, "錯誤": str(e), "狀態": "錯誤", "ATR": 0}

# --- 側邊欄 自動化 選單 ---
st.sidebar.info("戰略 狀態：Keep 實彈 優先")
target_list = st.sidebar.selectbox("請 選擇 監控 抽屜", list(MONITOR_LISTS.keys()))

if st.sidebar.button(f"啟動 {target_list} 實彈 總攻"):
    with st.spinner(f"正在 物理 校準 {target_list} 數據 並 執行 排序..."):
        results = []
        for s in MONITOR_LISTS[target_list]:
            res = get_jyw_metrics(s)
            results.append(res)
        
        if results:
            st.success(f"{target_list} 實彈 歸位！")
            df_final = pd.DataFrame(results)
            
            # --- 1.08 級別 物理 排序 協議 [cite: 2026-03-24] ---
            # 優先級 1：狀態 (高效優先)
            # 優先級 2：名稱 (確保 ★★★ 在最上面)
            # 優先級 3：ATR (波動大優先)
            df_sorted = df_final.sort_values(
                by=['狀態', '名稱', 'ATR'], 
                ascending=[True, False, False]
            )
            
            st.table(df_sorted)
        else:
            st.error("物理 斷線：代號 格式 有誤。")
