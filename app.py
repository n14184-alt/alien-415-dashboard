import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import yfinance as yf # 物理 性 地 抓取 歷史 20 週 數據 ！！

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 曾氏五線譜", layout="wide")

# --- 側邊 欄 ： 物理 參數 鎖定 ---
st.sidebar.header("🕹️ 曾 氏 20 週 核心 控制")
tseng_unit = st.sidebar.number_input("物理 曾 氏 間距 單位 (%)", value=2.5, step=0.1)
window = 100 # 物理 性 地 鎖定 20 週 ( 100 交易日 ) [cite: 2026-03-28]

# --- 數據 引擎 ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

@st.cache_data(ttl=300)
def get_live_data():
    df = pd.read_csv(URL_FUND)
    df.columns = [c.replace(' ', '').replace('　', '') for c in df.columns]
    return df

# --- 真正的 曾 氏 畫圖 引擎 ---
def plot_real_tseng(name, symbol, current_price):
    try:
        # 1. 物理 性 地 抓取 歷史 100 天 ( 20 週 ) 數據 
        hist = yf.download(symbol, period="150d") # 多 抓 一點 確保 有 100 天
        prices = hist['Close'].tail(window).values
        x = np.arange(len(prices))
        
        # 2. 物理 性的 「 線性 迴歸 」 生成 直直 的 曾 氏 均線 [cite: 2026-03-28]
        slope, intercept = np.polyfit(x, prices, 1)
        central_line = slope * x + intercept
        
        # 3. 物理 性的 「 五 線 譜 」 間距 計算
        unit = current_price * (tseng_unit / 100)
        
        fig = go.Figure()
        # 繪製 歷史 價格 軌跡
        fig.add_trace(go.Scatter(x=x, y=prices, name="歷史 彈道", line=dict(color='#FFD700', width=1.5)))
        # 繪製 直直 的 5 條 線 [cite: 2026-03-28]
        fig.add_trace(go.Scatter(x=x, y=central_line + 2*unit, name="極度 樂觀", line=dict(color='#145a32', dash='dot')))
        fig.add_trace(go.Scatter(x=x, y=central_line + unit, name="樂觀", line=dict(color='#145a32')))
        fig.add_trace(go.Scatter(x=x, y=central_line, name="曾 氏 均線", line=dict(color='#900c3f', width=2)))
        fig.add_trace(go.Scatter(x=x, y=central_line - unit, name="悲觀", line=dict(color='#581845')))
        fig.add_trace(go.Scatter(x=x, y=central_line - 2*unit, name="極度 悲觀", line=dict(color='#581845', dash='dot')))

        fig.update_layout(title=f"🎼 {name} ({symbol}) 20週 曾 氏 五 線 譜", template="plotly_dark")
        return fig
    except:
        return None

# --- 指揮部 噴發 ---
df_fund = get_live_data()
selected = st.selectbox("🎯 鎖定 標的", ["全域 噴發"] + list(df_fund['名稱']))

if selected == "全域 噴發":
    for i, row in df_fund.iterrows():
        # 物理 性 地 這裡 需要 您的 試算表 有 「 代碼 」 欄位 ( 如 0050.TW )
        fig = plot_real_tseng(row['名稱'], row['代碼'], row['當日股價'])
        if fig: st.plotly_chart(fig, use_container_width=True)
else:
    row = df_fund[df_fund['名稱'] == selected].iloc[0]
    fig = plot_real_tseng(row['名稱'], row['代碼'], row['當日股價'])
    if fig: st.plotly_chart(fig, use_container_width=True)
