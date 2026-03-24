import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("1.08 級別 實彈 監控：強勢優先模式") # 根據您最新介面同步

# --- 1.08 級別 實彈 對位 字典 (代號 + 名稱) ---
# 這裡 強制 將 代號 寫入 名稱 欄位，確保 視覺 直接 下單 [cite: 2026-03-24]
STOCK_NAME_MAP = {
    # --- 個股 (精選) ---
    "2330.TW": "2330 台積電 ★★★", "2891.TW": "2891 中信金", "2454.TW": "2454 聯發科 ★★★",
    "2412.TW": "2412 中華電", "2002.TW": "2002 中鋼", "2308.TW": "2308 台達電 ★★★",
    "2881.TW": "2881 富邦金", "1303.TW": "1303 南亞", "1216.TW": "1216 統一", "4904.TW": "4904 遠傳",
    
    # --- ETF (56) 實彈 對位 裝填 ---
    "00913.TW": "00913 中信臺灣智慧50", "00830.TW": "00830 國泰費城半導體", "00899.TW": "00899 關鍵半導體",
    "00733.TW": "00733 富邦臺灣中小", "00891.TW": "00891 中信關鍵半導體", "0061.TW": "0061 元大寶滬深",
    "00660.TW": "00660 元大歐洲50", "00918.TW": "00918 大華優利高填息", "00991A.TW": "00991A IC設計",
    "00885.TW": "00885 富邦越南", "00940.TW": "00940 元大台灣價值高息", "00988A.TW": "00988A 半導體設備",
    "00892.TW": "00892 富邦台灣半導體", "00960.TW": "00960 野村全球航運", "00652.TW": "00652 富邦印度",
    "0056.TW": "0056 元大高股息", "00642U.TW": "00642U 元大S&P原油", "00965.TW": "00965 中信全球高股息",
    "00878.TW": "00878 國泰永續高股息", "0052.TW": "0052 富邦科技", "00894.TW": "00894 中信小資高價30",
    "00713.TW": "00713 元大台灣高息低波", "00981A.TW": "00981A 全球AI", "00909.TW": "00909 國泰數位支付",
    "00941.TW": "00941 中信上游半導體", "0050.TW": "0050 元大台灣50", "00682U.TW": "00682U 元大S&P黃金",
    "00910.TW": "00910 依德恩AI", "009805.TW": "009805 美債20Y", "00635U.TW": "00635U 元大S&P標普500",
    "00735.TW": "00735 國泰日本ETF", "00919.TW": "00919 群益台灣精選高息", "00876.TW": "00876 元大未來關鍵科技",
    "00681R.TW": "00681R 元大美債反1", "00762.TW": "00762 元大全球AI", "00757.TW": "00757 統一FANG+",
    "0051.TW": "0051 元大中型100", "00924.TW": "00924 復華S&P500成長", "006201.TWO": "006201 元大富櫃50",
    "00928.TWO": "00928 中信上櫃ESG", "00875.TW": "00875 國泰網路網路", "00954.TW": "00954 中信低碳債",
    "00905.TW": "00905 FT臺灣Smart", "00668.TW": "00668 國泰美國道瓊", "00662.TW": "00662 富邦NASDAQ",
    "00646.TW": "00646 元大S&P500", "00770.TW": "00770 國泰北美科技", "00861.TW": "00861 元大全球未來通訊",
    "00963.TW": "00963 中信全球ESG高息", "00964.TW": "00964 中信亞太高股息", "00971.TW": "00971 中信全球趨勢"
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
    "ETF (56)": list(STOCK_NAME_MAP.keys())[10:], 
    "個股 (精選)": list(STOCK_NAME_MAP.keys())[:10]
}

def get_jyw_metrics(symbol):
    try:
        ticker = str(symbol).strip().upper()
        # 自動 判定 顯示 名稱，若 字典 沒定義 則 顯示 代號
        display_name = STOCK_NAME_MAP.get(ticker, ticker)
        data = yf.Ticker(ticker)
        df = data.history(period="60d")
        
        if df.empty or len(df) < 15:
            return {"名稱": display_name, "收盤": 0, "ATR": 0, "狀態": "未知"}
            
        high_low = df['High'] - df['Low']
        atr = high_low.rolling(14).mean().iloc[-1]
        close = df['Close'].iloc[-1]
        
        status = "高效" if close > (df['Close'].iloc[-2] - 2*atr) else "低效"
        
        return {
            "名稱": display_name, "收盤": round(close, 2),
            "ATR": round(atr, 2), "狀態": status
        }
    except Exception as e:
        return {"名稱": symbol, "收盤": 0, "ATR": 0, "狀態": "錯誤"}

# --- 側邊欄 ---
st.sidebar.info("戰略 狀態：保持實彈優先") # 同步最新標籤
target_list = st.sidebar.selectbox("請選擇監控公桌", list(MONITOR_LISTS.keys()))

if st.sidebar.button(f"啟動 {target_list} 買進攻"): # 同步按鈕字樣
    with st.spinner(f"正在 物理 校準 {target_list} 數據 並 執行 能量 排序..."):
        results = []
        for s in MONITOR_LISTS[target_list]:
            res = get_jyw_metrics(s)
            results.append(res)
        
        if results:
            df_final = pd.DataFrame(results)
            df_final['狀態'] = pd.Categorical(
                df_final['狀態'], 
                categories=['高效', '低效', '未知', '錯誤'], 
                ordered=True
            )
            
            # 能量 排序 鎖定 [cite: 2026-03-24]
            df_sorted = df_final.sort_values(
                by=['狀態', 'ATR', '名稱'], 
                ascending=[True, False, False]
            ).reset_index(drop=True)
            
            st.table(df_sorted)
