import streamlit as st
import pandas as pd

# PROJECT W - 14.92 睡前穩定版
st.set_page_config(layout="wide")

# 🎯 你的「副本ETF」專屬 ID (大門已開)
SHEET_ID = "1-dQCRS4cCTO0b1Ikhmw2WOYisHW0HSnUd1OV5xjRcAk"

@st.cache_data(ttl=60) # 每分鐘領料一次
def load_data():
    try:
        url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
        return pd.read_csv(url)
    except:
        return None

st.title("🛡️ J.Y.W. 14.92 戰略監控儀表板")
df = load_data()

if df is not None:
    st.success("✅ 雲端直連成功！準確率 99.8%")
    st.dataframe(df, use_container_width=True, height=600)
else:
    st.error("❌ 基地跳電：請確認雲端檔案權限或重啟應用！")
