import streamlit as st
import pandas as pd
import requests

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="TWSE 實彈 指揮部", layout="wide")
st.title("🎯 1.08 級別：TWSE 數據 終極 擊穿")

# --- 物理 鎖定 您的 TWSE 網址 [cite: 2026-03-28] ---
TWSE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pubhtml?gid=1864273820&single=true"

def get_twse_final_fix():
    try:
        # 物理 性 的 「 數據 暴力 請求 」
        # 使用 pd.read_html 直接 暴力 讀取 網址
        all_tables = pd.read_html(TWSE_URL, header=1)
        
        if len(all_tables) > 0:
            df = all_tables[0] # 物理 性 抓取 第一 個 有效 表格
            st.success("💎 物理 顯影 ： 成功 擊穿 網頁 牆 ！！")
            st.dataframe(df, use_container_width=True, height=800)
        else:
            st.warning("⚠️ 物理 警示 ： 網頁 物理 性 地 沒 東西 ， 請 檢查 試算表 發佈 ！！")
            
    except Exception as e:
        st.error(f"物理 性 斷流 ： 網頁 穿透 最終 失敗 ！！ {e}")

# --- 啟動 買進 攻 ---
if st.button("啟動 TWSE 物理 擊穿"):
    with st.spinner("正在 物理 性 暴力 掃描 數據 ..."):
        get_twse_final_fix()
