import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 曾氏指揮部", layout="wide")
st.title("🎯 1.08 級別 ： 曾 氏 基金 實彈 模擬")

# --- 物理 鎖定 基金 彈道 ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

# --- 側邊 欄 指揮 區 ---
st.sidebar.header("🕹️ 曾 氏 戰略 控制")
# 物理 性 地 增加 您 要求 的 「 框框 」 ！！ [cite: 2026-03-28]
tseng_std = st.sidebar.number_input("物理 曾 氏 標準差 鎖定", min_value=0.1, max_value=5.0, value=2.0, step=0.1)

# --- 數據 引擎 ---
@st.cache_data(ttl=300)
def get_fund_data():
    df = pd.read_csv(URL_FUND)
    df.columns = [c.replace(' ', '').replace('　', '') for c in df.columns]
    return df

df_fund = get_fund_data()

# --- 曾 氏 直線 顯影 引擎 ---
def plot_tseng_straight(name, price):
    # 物理 性 地 模擬 「 直直 的 線 」 ( 使用 線性 迴歸 模擬 曾 氏 趨勢 ) [cite: 2026-03-28]
    # 這裡 暫時 以 20 點 模擬 趨勢 彈道
    x = np.arange(20)
    y_base = np.linspace(price*0.9, price, 20) # 模擬 往上 的 複利 趨勢
    
    # 計算 曾 氏 直線 ( 線性 趨勢 )
    slope, intercept = np.polyfit(x, y_base, 1)
    tseng_line = slope * x + intercept
    
    # 根據 您 輸入 的 框框 數字 計算 直直 的 通道 [cite: 2026-03-28]
    margin = price * (tseng_std / 100)
    upper_line = tseng_line + margin
    lower_line = tseng_line - margin

    fig = go.Figure()
    # 曾 氏 均線 ( 莊家 紅 )
    fig.add_trace(go.Scatter(x=x, y=tseng_line, name="曾 氏 趨勢 ( 紅 )", line=dict(color='#900c3f', width=2)))
    # 曾 氏 通道 ( 護盤 綠 ) - 物理 性 地 直直 的 線 ！！
    fig.add_trace(go.Scatter(x=x, y=upper_line, name="曾 氏 上 軌", line=dict(color='#145a32', width=1, dash='dot')))
    fig.add_trace(go.Scatter(x=x, y=lower_line, name="曾 氏 下 軌", line=dict(color='#145a32', width=1, dash='dot')))
    # 現價 點
    fig.add_trace(go.Scatter(x=[19], y=[price], mode='markers', name="當前 實彈", marker=dict(color='#FFD700', size=10)))

    fig.update_layout(title=f"📈 {name} 曾 氏 直線 顯影", template="plotly_dark", height=300, margin=dict(l=20, r=20, t=40, b=20))
    return fig

# --- 顯示 邏輯 ---
# 1. 單獨 顯示 選擇
selected_asset = st.selectbox("🎯 單獨 鎖定 基金 顯影", ["全域 噴發"] + list(df_fund['名稱'].unique()))

if selected_asset == "全域 噴發":
    # 2. 一次 顯示 多 支 ( 矩陣 佈局 ) [cite: 2026-03-28]
    cols = st.columns(2)
    for i, row in df_fund.iterrows():
        with cols[i % 2]:
            st.plotly_chart(plot_tseng_straight(row['名稱'], row['當日股價']), use_container_width=True)
else:
    # 3. 單獨 顯示 [cite: 2026-03-28]
    row = df_fund[df_fund['名稱'] == selected_asset].iloc[0]
    st.plotly_chart(plot_tseng_straight(row['名稱'], row['當日股價']), use_container_width=True)

st.success("💎 曾 氏 基金 抽屜 物理 噴發 完畢 ！！")
