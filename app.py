import streamlit as st
import pandas as pd

# [ 物理 鋼印 ] ： 1.08 級別 複利 帝國 雙 軌 指揮部
st.set_page_config(page_title="複利 帝國 指揮部", layout="wide")

# 物理 鎖定 ： 您的 兩條 物理 彈道 [cite: 2026-03-28]
# 請 確保 這 兩個 gid 都 已經 物理 性 地 「 發布 到 網路 」 並 設為 CSV 格式 ！！
URL_TWSE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=551908367&single=true&output=csv"
URL_OTC = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=1364531405&single=true&output=csv" # 範例 gid ， 請 替換 為 您的 上櫃 分頁 gid

st.title("🎯 複利 帝國 ： 實時 數據 顯影")

# 物理 性的 「 戰線 選擇器 」
market_mode = st.radio("物理 戰線 選擇", ["上市 TWSE", "上櫃 OTC"], horizontal=True)

target_url = URL_TWSE if market_mode == "上市 TWSE" else URL_OTC

try:
    # 物理 性的 「 暴力 讀取 」 ( 基金 成功 模式 [cite: 2026-03-28] )
    df = pd.read_csv(target_url)
    
    st.subheader(f"📈 物理 顯影 ： {market_mode} 實時 監控")
    st.dataframe(df, use_container_width=True, height=800)
    
    st.success(f"💎 物理 顯影 ： {market_mode} 數據 已經 物理 性 噴發 ！！")
except Exception as e:
    st.error(f"❌ 物理 性 斷流 ： {market_mode} 網址 權限 可能 未 開 ！！ \n 報錯 ： {e}")
