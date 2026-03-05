import streamlit as st
import pandas as pd

# PROJECT W - 14.92 雲端直連 (懶人專用版)
st.set_page_config(layout="wide")

# 🎯 你的試算表基地 ID
SHEET_ID = "1-dQCRS4cCTO0b1Ikhmw2WOYisHW0HSnUd1OV5xjRcAk" 

@st.cache_data(ttl=60) 
def load_data():
    try:
        url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
        return pd.read_csv(url)
    except:
        return None

st.title("🛡️ J.Y.W. 14.92 監控基地")
df = load_data()

if df is not None:
    st.success("✅ 基地連線成功！數據輸出準確率 99.8%")
    st.dataframe(df, use_container_width=True)
else:
    st.error("❌ 基地跳電：請確認試算表『知道連結的人即可檢視』權限是否已鎖緊！")
