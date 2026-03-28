import streamlit as st
import pandas as pd

# [ 物理 鋼印 ] ： 1.08 級別 雙 試算表 獨立 指揮部
st.set_page_config(page_title="複利 帝國 實彈 版圖", layout="wide")

# 物理 鎖定 ： 您 提供 的 兩條 獨立 物理 彈道 [cite: 2026-03-28]
URL_TWSE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=551908367&single=true&output=csv"
URL_OTC = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQQJErYh_DqHhxrKGswfAk7kgrw1D-mxkXCMoVw4tupugViWY4bVtA4HYur5JQ_znPi3lU5FkPvMkLl/pub?gid=1587848416&single=true&output=csv"

st.title("🏹 複利 帝國 ： 上市 / 上櫃 雙 軌 顯影")

# 物理 性的 「 戰線 切換 」
market = st.sidebar.radio("🔭 物理 戰線 選擇", ["上市 TWSE", "上櫃 OTC"])

target_url = URL_TWSE if market == "上市 TWSE" else URL_OTC

try:
    # 物理 性的 「 暴力 穿透 」 ( 採用 基金 成功 模式 [cite: 2026-03-28] )
    df = pd.read_csv(target_url)
    
    st.header(f"📊 {market} 實時 物理 監控")
    
    # 物理 性的 「 莊家 樣式 」 渲染
    st.dataframe(df, use_container_width=True, height=800)
    
    st.success(f"💎 物理 顯影 ： {market} 彈道 噴發 成功 ！！")
    
except Exception as e:
    st.error(f"❌ 物理 性 斷流 ： {market} 請求 失敗 ！！ \n 原因 ： {e}")
