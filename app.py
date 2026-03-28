import streamlit as st
import pandas as pd

# [ 物理 鋼印 ] ： 1.08 級別 TWSE 實彈 指揮部
st.set_page_config(page_title="TWSE 實彈 指揮部", layout="wide")

# 物理 鎖定 ： 這是 您 剛才 指定 的 最終 CSV 彈道 [cite: 2026-03-28]
TWSE_FINAL_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=551908367&single=true&output=csv"

st.title("🎯 1.08 級別：TWSE 數據 實時 顯影")

try:
    # 物理 性的 「 暴力 讀取 」 ( 採用 基金 成功 模式 [cite: 2026-03-28] )
    df = pd.read_csv(TWSE_FINAL_URL)
    
    # 物理 性的 「 基金 樣式 」 渲染 [cite: 2026-03-28]
    st.subheader("📈 物理 顯影 ： TWSE 實時 股價 監控")
    
    # 使用 您 滿意 的 基金 顯示 方式
    st.dataframe(df, use_container_width=True, height=800)
    
    st.success("💎 物理 顯影 ： 恭喜 老闆 ！！ 股價 數據 已經 物理 性 噴發 ！！")
except Exception as e:
    st.error(f"❌ 物理 性 斷流 ： 網址 穿透 失敗 ！！ \n 報錯 內容 ： {e}")
