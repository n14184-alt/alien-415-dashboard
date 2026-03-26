import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("🎯 1.08 級別：J.Y.W. 綜合 實彈 指揮部")

# --- 物理 鎖定 基金 實彈 彈道 [cite: 2026-03-25] ---
FUND_PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

# --- ETF/個股 對位 字典 ---
STOCK_NAME_MAP = {
    "2330.TW": "2330 台積電 ★★★", "2891.TW": "2891 中信金", "2454.TW": "2454 聯發科 ★★★",
    "2412.TW": "2412 中華電", "2002.TW": "2002 中鋼", "2308.TW": "2308 台達電 ★★★",
    "2881.TW": "2881 富邦金", "1303.TW": "1303 南亞", "1216.TW": "1216 統一", "4904.TW": "4904 遠傳",
    "00913.TW": "00913 兆豐台灣晶圓製造", "00830.TW": "00830 國泰費城半導體", "00899.TW": "00899 FT潔淨能源",
    "00733.TW": "00733 富邦臺灣中小", "00891.TW": "00891 中信關鍵半導體", "0061.TW": "0061 元大寶滬深",
    "00660.TW": "00660 元大歐洲50", "00918.TW": "00918 大華優利高填息", "00991A.TW": "00991A 主動復華未來50",
    "00885.TW": "00885 富邦越南", "00940.TW": "00940 元大台灣價值高息", "00988A.TW": "00988A 主動統一全球創新",
    "00892.TW": "00892 富邦台灣半導體", "00960.TW": "00960 野村全球航運", "00652.TW": "00652 富邦印度",
    "0056.TW": "0056 元大高股息", "00642U.TW": "00642U 元大S&P原油", "00965.TW": "00965 元大航太防衛科技",
    "00878.TW": "00878 國泰永續高股息", "0052.TW": "0052 富邦科技", "00894.TW": "00894 中信小資高價30",
    "00713.TW": "00713 元大台灣高息低波", "00981A.TW": "00981A 主動統一台股增長", "00909.TW": "00909 國泰數位支付",
    "00941.TW": "00941 中信上游半導體", "0050.TW": "0050 元大台灣50", "00682U.TW": "00682U 期元大美元指數",
    "00910.TW": "00910 第一金太空衛星", "009805.TW": "009805 新光美國電力基建", "00635U.TW": "00635U 期元大S&P黃金",
    "00735.TW": "00735 國泰臺韓科技", "00919.TW": "00919 群益台灣精選高息", "00876.TW": "00876 元大全球5G",
    "00681R.TW": "00681R 元大美債反1", "00762.TW": "00762 元大全球AI", "00757.TW": "00757 統一FANG+",
    "0051.TW": "0051 元大中型100", "00924.TW": "00924 復華S&P500成長", "006201.TWO": "006201 元大富櫃50",
    "00928.TWO": "00928 中信上櫃ESG", "00875.TW": "00875 國泰網路網路", "00954.TW": "00954 中信日本半導體",
    "00905.TW": "00905 FT臺灣Smart", "00668.TW": "00668 國泰美國道瓊", "00662.TW": "00662 富邦NASDAQ",
    "00646.TW": "00646 元大S&P500", "00770.TW": "00770 國泰北美科技", "00861.TW": "00861 元大全球未來通訊",
    "00963.TW": "00963 中信全球高股息", "00964.TW": "00964 中信亞太高股息", "00971.TW": "00971 野村美國研發龍頭"
}

# --- 物理 裝填 區 ---
MONITOR_LISTS = {
    "ETF (56)": list(STOCK_NAME_MAP.keys())[10:], 
    "個股 (精選)": list(STOCK_NAME_MAP.keys())[:10],
    "基金 (28)": ["PUB_SHEET_TRIGGER"] # 指向 試算表 彈道
}

# --- 舊 引擎： 處理 ETF/個股 (yfinance) ---
def get_stock_metrics(symbol):
    try:
        ticker = str(symbol).strip().upper()
        display_name = STOCK_NAME_MAP.get(ticker, ticker)
        data = yf.Ticker(ticker)
        df = data.history(period="60d")
        if df.empty or len(df) < 15:
            return {"名稱": display_name, "收盤": 0, "ATR": 0, "狀態": "未知"}
        high_low = df['High'] - df['Low']
        atr = high_low.rolling(14).mean().iloc[-1]
        close = df['Close'].iloc[-1]
        status = "高效" if close > (df['Close'].iloc[-2] - 2*atr) else "低效"
        return {"名稱": display_name, "收盤": round(close, 2), "ATR": round(atr, 2), "狀態": status}
    except:
        return {"名稱": symbol, "收盤": 0, "ATR": 0, "狀態": "錯誤"}

# --- 新 引擎： 處理 基金 (pubhtml) [cite: 2026-03-25] ---
def get_fund_metrics_from_sheet():
    try:
        df = pd.read_csv(FUND_PUB_URL)
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        # 物理 運算 ATR (變動率)
        df['ATR'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        # 格式 統一 對位
        df_res = df[['名稱', '當日股價', 'ATR']].copy()
        df_res.columns = ['名稱', '收盤', 'ATR']
        df_res['狀態'] = df_res['ATR'].apply(lambda x: "高效" if x > 0 else "低效")
        return df_res
    except:
        return None

# --- 側邊欄 ---
st.sidebar.info("戰略 狀態：保持實彈優先")
target_list = st.sidebar.selectbox("請選擇監控公桌", list(MONITOR_LISTS.keys()))

if st.sidebar.button(f"啟動 {target_list} 買進攻"):
    with st.spinner(f"正在 物理 校準 {target_list} 數據..."):
        if target_list == "基金 (28)":
            df_final = get_fund_metrics_from_sheet()
        else:
            results = [get_stock_metrics(s) for s in MONITOR_LISTS[target_list]]
            df_final = pd.DataFrame(results)

        if df_final is not None:
            # 視覺 渲染 邏輯 [cite: 2026-02-18]
            def style_atr(val):
                if val > 0.5: return 'background-color: #900c3f; color: white; font-weight: bold'
                elif val < -0.5: return 'background-color: #145a32; color: #d4edda;'
                return ''
            
            # 能量 排序 鎖定
            df_sorted = df_final.sort_values(by='ATR', ascending=False).reset_index(drop=True)
            st.dataframe(df_sorted.style.applymap(style_atr, subset=['ATR']), use_container_width=True, height=800)
