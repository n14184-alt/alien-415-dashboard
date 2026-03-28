import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 曾氏五線譜", layout="wide")
st.title("🎯 1.08 級別 ： 曾 氏 五 線 譜 實彈 指揮部")

# --- 物理 鎖定 基金 彈道 ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

# --- 側邊 欄 指揮 區 ---
st.sidebar.header("🕹️ 曾 氏 五 線 譜 控制")
# 物理 性 地 解決 「 0.5 太小 」 的 問題 ！！ [cite: 2026-03-28]
# 您 可以 填 2.5 或 5.0， 物理 性 地 瞬間 撐開 5 條 線 ！！
tseng_unit = st.sidebar.number_input("物理 曾 氏 間距 單位 (%)", min_value=0.1, max_value=10.0, value=2.5, step=0.1)

# --- 數據 引擎 ---
@st.cache_data(ttl=300)
def get_fund_data():
    try:
        df = pd.read_csv(URL_FUND)
        df.columns = [c.replace(' ', '').replace('　', '') for c in df.columns]
        return df
    except:
        return pd.DataFrame()

df_fund = get_fund_data()

# --- 曾 氏 五 線 譜 顯影 引擎 ---
def plot_tseng_five_lines(name, price):
    # 物理 性 地 模擬 「 直直 的 5 條 線 」 [cite: 2026-03-28]
    x = np.arange(20)
    # 模擬 複利 趨勢 彈道
    y_base = np.linspace(price*0.95, price, 20) 
    slope, intercept = np.polyfit(x, y_base, 1)
    central_line = slope * x + intercept
    
    # 物理 性的 「 5 線 階層 」 計算 [cite: 2026-03-28]
    unit = price * (tseng_unit / 100)
    line_up_2 = central_line + (unit * 2) # 極度 樂觀 ( 綠 )
    line_up_1 = central_line + unit       # 樂觀 ( 綠 )
    line_low_1 = central_line - unit      # 悲觀 ( 紅 )
    line_low_2 = central_line - (unit * 2)# 極度 悲觀 ( 紅 )

    fig = go.Figure()
    
    # 畫出 5 條 直直 的 線 ！！ [cite: 2026-03-28]
    colors = {'high': '#145a32', 'mid': '#900c3f', 'low': '#581845'}
    
    fig.add_trace(go.Scatter(x=x, y=line_up_2, name="極度 樂觀", line=dict(color=colors['high'], width=1, dash='dot')))
    fig.add_trace(go.Scatter(x=x, y=line_up_1, name="樂觀", line=dict(color=colors['high'], width=1)))
    fig.add_trace(go.Scatter(x=x, y=central_line, name="曾 氏 均線", line=dict(color=colors['mid'], width=2)))
    fig.add_trace(go.Scatter(x=x, y=line_low_1, name="悲觀", line=dict(color=colors['low'], width=1)))
    fig.add_trace(go.Scatter(x=x, y=line_low_2, name="極度 悲觀", line=dict(color=colors['low'], width=1, dash='dot')))
    
    # 現價 實彈 點
    fig.add_trace(go.Scatter(x=[19], y=[price], mode='markers+text', name="實彈", 
                             text=[f"{price}"], textposition="top center",
                             marker=dict(color='#FFD700', size=12, symbol='diamond')))

    fig.update_layout(title=f"🎼 {name} 曾 氏 五 線 譜", template="plotly_dark", height=400, 
                      margin=dict(l=20, r=20, t=50, b=20), hovermode="x unified")
    return fig

# --- 顯示 邏輯 ---
if not df_fund.empty:
    selected_asset = st.selectbox("🎯 選擇 鎖定 標的", ["全域 五 線 譜 噴發"] + list(df_fund['名稱'].unique()))

    if selected_asset == "全域 五 線 譜 噴發":
        cols = st.columns(2)
        for i, row in df_fund.iterrows():
            with cols[i % 2]:
                st.plotly_chart(plot_tseng_five_lines(row['名稱'], row['當日股價']), use_container_width=True)
    else:
        row = df_fund[df_fund['名稱'] == selected_asset].iloc[0]
        st.plotly_chart(plot_tseng_five_lines(row['名稱'], row['當日股價']), use_container_width=True)
