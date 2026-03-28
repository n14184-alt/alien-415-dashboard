import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import yfinance as yf

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 曾氏指揮部", layout="wide")
st.title("🎯 1.08 級別 ： 曾 氏 20 週 實彈 終極 壓測")

# --- 側邊 欄 ： 物理 參數 ---
st.sidebar.header("🕹️ 曾 氏 核心 控制")
tseng_unit = st.sidebar.number_input("物理 曾 氏 間距 單位 (%)", value=2.5, step=0.1)
window = 100 # 物理 性 鎖定 20 週 ( 100 交易日 )

# --- 數據 引擎 ( 鋼鐵 容錯 版 ) ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

@st.cache_data(ttl=60)
def get_safe_data():
    try:
        df = pd.read_csv(URL_FUND)
        df.columns = [c.strip().replace('　', '') for c in df.columns]
        # 物理 性 自動 偵測 「 代碼 」 抽屜
        code_col = next((c for c in df.columns if any(x in c for x in ['代碼', '代號', 'Symbol', 'Ticker'])), None)
        name_col = next((c for c in df.columns if any(x in c for x in ['名稱', 'Name', '基金'])), df.columns[0])
        price_col = next((c for c in df.columns if any(x in c for x in ['股價', '價格', 'Price'])), None)
        
        if code_col: df['target_code'] = df[code_col].astype(str)
        return df, name_col, price_col
    except: return pd.DataFrame(), None, None

# --- 物理 實彈 繪圖 ---
def plot_tseng_final(name, symbol, current_price):
    try:
        # 物理 性 借調 歷史 20 週
        hist = yf.download(symbol, period="180d", progress=False)
        if hist.empty: return None
        prices = hist['Close'].tail(window).values.flatten()
        x = np.arange(len(prices))
        
        # 線性 迴歸 ( 曾 氏 直線 )
        slope, intercept = np.polyfit(x, prices, 1)
        base_line = slope * x + intercept
        
        # 五 線 譜 物理 間距
        unit = current_price * (tseng_unit / 100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=prices, name="歷史 軌跡", line=dict(color='#FFD700', width=2)))
        for i, (m, label, clr) in enumerate([(2,'極度樂觀','#145a32'), (1,'樂觀','#145a32'), (0,'均線','#900c3f'), (-1,'悲觀','#581845'), (-2,'極度悲觀','#581845')]):
            fig.add_trace(go.Scatter(x=x, y=base_line + i*unit if i==0 else base_line + m*unit, 
                                     name=label, line=dict(color=clr, width=1 if abs(m)==1 else 2, dash='dot' if abs(m)==2 else 'solid')))
        
        fig.update_layout(title=f"🎼 {name} ({symbol}) 曾 氏 五 線 譜", template="plotly_dark", height=450)
        return fig
    except: return None

# --- 執行 噴發 ---
df, n_col, p_col = get_safe_data()
if not df.empty and 'target_code' in df.columns:
    target = st.selectbox("🎯 鎖定 標的", ["全域 壓測"] + list(df[n_col]))
    if target == "全域 壓測":
        for _, row in df.iterrows():
            f = plot_tseng_final(row[n_col], row['target_code'], row[p_col] if p_col else 100)
            if f: st.plotly_chart(f, use_container_width=True)
    else:
        row = df[df[n_col] == target].iloc[0]
        f = plot_tseng_final(row[n_col], row['target_code'], row[p_col] if p_col else 100)
        if f: st.plotly_chart(f, use_container_width=True)
st.info("💎 1.08 級別 物理 指揮部 壓測 完畢 。")
