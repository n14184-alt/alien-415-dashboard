import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import yfinance as yf

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 曾氏五線譜", layout="wide")
st.title("🎯 1.08 級別 ： 曾 氏 20 週 五 線 譜 實彈 版")

# --- 側邊 欄 ： 物理 參數 鎖定 ---
st.sidebar.header("🕹️ 曾 氏 20 週 核心 控制")
tseng_unit = st.sidebar.number_input("物理 曾 氏 間距 單位 (%)", value=2.5, step=0.1)
window = 100 # 物理 性 地 鎖定 20 週 ( 100 交易日 )

# --- 數據 引擎 ( 增加 欄位 容錯 ) ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

@st.cache_data(ttl=300)
def get_live_data():
    try:
        df = pd.read_csv(URL_FUND)
        # 物理 性 地 清理 欄位 空格
        df.columns = [c.replace(' ', '').replace('　', '') for c in df.columns]
        
        # 物理 性的 「 代碼 欄位 識別 引擎 」 ！！
        code_col = None
        for col in ['代碼', '股票代號', '基金代號', '代號', 'Symbol']:
            if col in df.columns:
                code_col = col
                break
        
        if code_col:
            df['target_code'] = df[code_col]
        else:
            st.error("❌ 物理 性 警報 ： 找不到 代碼 欄位 ， 請 檢查 試算表 ！！")
            
        return df
    except Exception as e:
        st.error(f"❌ 數據 讀取 失敗 ： {e}")
        return pd.DataFrame()

# --- 實彈 畫圖 引擎 ---
def plot_real_tseng(name, symbol, current_price):
    try:
        # 物理 性 地 抓取 歷史 100 天 ( 20 週 )
        hist = yf.download(str(symbol), period="180d")
        if hist.empty: return None
        
        prices = hist['Close'].tail(window).values
        x = np.arange(len(prices))
        
        # 曾 氏 直線 ( 線性 迴歸 )
        slope, intercept = np.polyfit(x, prices, 1)
        central_line = slope * x + intercept
        
        # 間距 計算
        unit = current_price * (tseng_unit / 100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=prices, name="歷史 彈道", line=dict(color='#FFD700', width=2)))
        fig.add_trace(go.Scatter(x=x, y=central_line + 2*unit, name="極度 樂觀", line=dict(color='#145a32', dash='dot')))
        fig.add_trace(go.Scatter(x=x, y=central_line + unit, name="樂觀", line=dict(color='#145a32')))
        fig.add_trace(go.Scatter(x=x, y=central_line, name="曾 氏 均線", line=dict(color='#900c3f', width=2)))
        fig.add_trace(go.Scatter(x=x, y=central_line - unit, name="悲觀", line=dict(color='#581845')))
        fig.add_trace(go.Scatter(x=x, y=central_line - 2*unit, name="極度 悲觀", line=dict(color='#581845', dash='dot')))

        fig.update_layout(title=f"🎼 {name} ({symbol}) 20週 曾 氏 五 線 譜", template="plotly_dark", height=500)
        return fig
    except:
        return None

# --- 指揮部 噴發 ---
df_fund = get_live_data()

if not df_fund.empty:
    name_col = '名稱' if '名稱' in df_fund.columns else df_fund.columns[0]
    selected = st.selectbox("🎯 鎖定 標的", ["全域 噴發"] + list(df_fund[name_col]))

    if selected == "全域 噴發":
        for i, row in df_fund.iterrows():
            fig = plot_real_tseng(row[name_col], row['target_code'], row['當日股價'])
            if fig: st.plotly_chart(fig, use_container_width=True)
    else:
        row = df_fund[df_fund[name_col] == selected].iloc[0]
        fig = plot_real_tseng(row[name_col], row['target_code'], row['當日股價'])
        if fig: st.plotly_chart(fig, use_container_width=True)
