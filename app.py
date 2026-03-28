import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="TWSE 實彈 指揮部", layout="wide")
st.title("🎯 1.08 級別：TWSE 試算表 暴力 顯影")

# --- 物理 鎖定 您 的 TWSE pubhtml 網址 [cite: 2026-03-28] ---
TWSE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pubhtml?gid=1864273820&single=true"

def get_twse_data_vision():
    try:
        # 物理 性的 「 暴力 穿透 」 網頁 格式
        response = requests.get(TWSE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 物理 性 地 尋找 網頁 中 的 表格 ( Table )
        tables = pd.read_html(str(soup.find_all('table')[0]))
        df = tables[0]
        
        # 物理 性的 「 格式 清理 」 ( 移除 Google 預設 的 多餘 欄位 )
        df.columns = df.iloc[1] # 物理 性 鎖定 第二 行 為 標題
        df = df.iloc[2:].reset_index(drop=True)
        
        st.subheader("📊 物理 顯影：TWSE 分頁 實時 股價")
        
        # 物理 性的 「 基金 樣式 」 渲染 [cite: 2026-03-28]
        st.dataframe(df, use_container_width=True, height=800)
        return True
    except Exception as e:
        st.error(f"物理 性 斷流 ： 網頁 穿透 失敗 ！！ {e}")
        return False

# --- 啟動 買進 攻 ---
if st.button("啟動 TWSE 暴力 顯影"):
    with st.spinner("正在 物理 性 擊穿 網頁 數據 ..."):
        get_twse_data_vision()
