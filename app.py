import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="TWSE 實彈 穿透", layout="wide")

# --- 物理 鎖定 ： 直接 抓 試算表 內容 [cite: 2026-03-28] ---
# 丫環 物理性 地 提醒 ： 請 務必 使用 結尾 為 output=csv 的 網址 ！！
TWSE_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=1864273820&single=true&output=csv"

st.title("🏹 物理 穿透 ： TWSE 試算表 直連")

try:
    # 物理 性的 「 暴力 讀取 」 ： 不 廢話 ， 直接 抓 ！！
    df = pd.read_csv(TWSE_CSV_URL)
    
    # 物理 性的 「 基金 樣式 」 顯影
    st.dataframe(df, use_container_width=True, height=800)
    
    st.success("💎 物理 顯影 ： 試算表 內容 已經 物理 性 噴發 ！！")
except Exception as e:
    st.error(f"物理 性 斷流 ： 網址 還是 不對 ！！ {e}")
