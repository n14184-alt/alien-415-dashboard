import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="TWSE 實彈 指揮部", layout="wide")
st.title("🎯 1.08 級別：TWSE 試算表 實時 顯影")

# --- 物理 鎖定 您 指定 的 TWSE 試算表 網址 [cite: 2026-03-28] ---
# 注意：這裡 使用 您 提供 的 CSV 導出 格式
TWSE_PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=1864273820&single=true&output=csv"

# --- 物理 顯影 引擎 [cite: 2026-03-28] ---
def get_twse_metrics():
    try:
        # 物理 性 地 讀取 您 的 TWSE 分頁
        df = pd.read_csv(TWSE_PUB_URL)
        
        # 物理 性 格式 化 ( 確保 欄位 對位 基金 樣式 )
        # 假設 您的 試算表 欄位 包含 '名稱' 與 '股價' ( 或 類似 標籤 )
        st.subheader("📊 物理 顯影：實時 股價 監控")
        
        # 視覺 渲染 邏輯 [cite: 2026-02-18]
        def style_positive(val):
            try:
                num = float(val)
                if num > 0: return 'color: #900c3f; font-weight: bold'
                elif num < 0: return 'color: #145a32;'
            except: pass
            return ''
            
        # 物理 性 地 像 基金 一樣 顯示 表格
        st.dataframe(df.style.applymap(style_positive), use_container_width=True, height=800)
        return True
    except Exception as e:
        st.error(f"物理 性 斷流 ： 找不到 數據 或 網址 錯誤 ！！ {e}")
        return False

# --- 啟動 買進 攻 ---
if st.button("啟動 TWSE 物理 顯影"):
    with st.spinner("正在 物理 性 穿透 試算表 數據 ..."):
        get_twse_metrics()
