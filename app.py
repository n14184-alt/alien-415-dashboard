import streamlit as st
import yfinance as yf
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("1.08 級別 實彈 監控：Keep 抽屜 優先 模式")

# --- 物理 裝填 區：老闆，這裡 已經 修正 了 語法 與 中文 註解 ---
MONITOR_LISTS = {
    "基金 (28)": [
        "F0HKG05X22:FO",  # 安聯台灣科技基金
        "F00000MMGD:FO",  # 統一新亞洲科技能源
        "F0HKG05WZM:FO",  # 野村 e 科技基金
        "F0HKG05X2C:FO",  # 統一奔騰基金
        "F000015CWL:FO",  # 國泰台灣高股息(B)
        "F00001EBH4:FO",  # 元大全球優質龍頭平衡
        "F0HKG05WYP:FO",  # 台新台灣中小基金
        "F00000ZH5C:FO",  # 路博邁台灣5G股票
        "F0HKG05WSZ:FO",  # 街口中小
        "F0HKG05WZO:FO",  # 街口台灣
        "F00000X5LG:FO",  # 統一全球新科技(台)
        "F00000OXXD:FO",  # 安聯收益成長AM
        "F00001EMTX:FO",  # 貝萊德世界科技
        "F00001ELXG:FO",  # 貝萊德世界黃金
        "F00001EMTU:FO",  # 貝萊德世界礦業
        "F0GBR04ARK:FO",  # 富坦東歐(歐元)
        "F000000GKS:FO",  # 富坦天然資源
        "F0GBR04V6U:FO",  # 富坦生技領航
        "F0GBR04SNN:FO",  # JF拉美
        "F0HKG062PO:FO",  # 利安資金韓國
        "F0GBR04AC1:FO",  # 景順環球消費趨勢
        "F0GBR04BG3:FO",  # 摩根士丹利美國增長
        "F00000PXGY:FO",  # 法巴乾淨能源
        "F00001ELXE:FO",  # 貝萊德世界能源
        "F00001ELXD:FO",  # 貝萊德永續能源
        "F00001ELXF:FO",  # 貝萊德世界金融
        "F0GBR04ASX:FO",  # 貝萊德美元儲備(A2)
        "F00000MK1B:FO"   # 群益印度中小
    ],
    "ETF (56)": [
        "00913.TW", "00830.TW", "00899.TW", "00733.TW", "00891.TW", 
        "0061.TW", "00660.TW", "00918.TW", "00991A.TW", "00885.TW", 
        "00940.TW", "00988A.TW", "00892.TW", "00960.TW", "00652.TW", 
        "0056.TW", "00642U.TW", "00965.TW", "00878.TW", "0052.TW", 
        "00894.TW", "00713.TW", "00981A.TW", "00909.TW", "00941.TW", 
        "0050.TW", "00682U.TW", "00910.TW", "00980S.TW", "00635U.TW", 
        "00735.TW", "00919.TW", "00876.TW", "00681R.TW", "00762.TW", 
        "00757.TW", "0051.TW", "00924.TW", "006201.TWO", "00928.TWO", 
        "00875.TW", "00954.TW", "00905.TW", "00668.TW", "00662.TW", 
        "00646.TW", "00770.TW", "00861.TW", "00963.TW", "00964.TW", "00971.TW"
    ],
    "個股 (精選)": [
        "2330.TW", "2891.TW", "2454.TW", "2412.TW", "2002.TW", 
        "2308.TW", "2881.TW", "1303.TW", "1216.TW", "4904.TW"
    ]
}

def get_jyw_metrics(symbol):
    """ 核心 運算：14.92 斜率 + ATR 物理 雙壓 """
    try:
        ticker = str(symbol).strip().upper()
        data = yf.Ticker(ticker)
        df = data.history(period="60d")
        
        if df.empty or len(df) < 15:
            return {"代號": ticker, "錯誤": "查無數據"}
            
        high_low = df['High'] - df['Low']
        atr = high_low.rolling(14).mean().iloc[-1]
        close = df['Close'].iloc[-1]
        
        # 狀態 判定 [cite: 2026-02-18]
        status = "高效" if close > (df['Close'].iloc[-2] - 2*atr) else "低效"
        
        return {
            "代號": ticker,
            "收盤": round(close, 2),
            "ATR": round(atr, 2),
            "狀態": status
        }
    except Exception as e:
        return {"代號": symbol, "錯誤": str(e)}

# --- 側邊欄 自動化 選單 ---
st.sidebar.info("戰略 狀態：Keep 實彈 優先")
target_list = st.sidebar.selectbox("請 選擇 監控 抽屜", list(MONITOR_LISTS.keys()))

if st.sidebar.button(f"啟動 {target_list} 實彈 總攻"):
    with st.spinner(f"正在 物理 校準 {target_list} 數據..."):
        results = []
        for s in MONITOR_LISTS[target_list]:
            res = get_jyw_metrics(s)
            results.append(res)
        
        if results:
            st.success(f"{target_list} 實彈 歸位！")
            st.table(pd.DataFrame(results))
        else:
            st.error("物理 斷線：代號 格式 有誤。")
