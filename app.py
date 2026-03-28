import streamlit as st
import pandas as pd

# [ 物理 鋼印 ] ： 1.08 級別 單一 分頁 測試
st.set_page_config(page_title="TWSE 物理 測試", layout="wide")

# 物理 鎖定 ： 這是 您 指定 的 TWSE 單一 分頁 CSV 網址 [cite: 2026-03-28]
TEST_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=1864273820&single=true&output=csv"

st.title("🎯 TWSE 物理 直連 測試")

try:
    # 物理 性的 「 暴力 讀取 」
    df = pd.read_csv(TEST_URL)
    
    st.success("💎 物理 顯影 ： 恭喜 老闆 ！！ 數據 已經 物理 性 穿透 ！！")
    st.dataframe(df, use_container_width=True, height=800)
    
except Exception as e:
    st.error(f"❌ 物理 性 斷流 ： 網址 依然 拒絕 穿透 ！！ \n 報錯 內容 ： {e}")
    st.info("老闆 ， 物理性 地 說 ， 如果 這裡 還是 報錯 ， 代表 試算表 的 『 發佈 』 權限 物理 性 地 沒 開好 ！！")
