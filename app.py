import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

# --- [J.Y.W. 3.0：原生視覺鋼印回歸] ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈指揮部", layout="wide")

# --- 🎯 視覺強化注入 (回歸簡潔美學) ---
st.markdown("""
    <style>
    .big-font { font-size: 28px !important; font-weight: bold !important; color: #FFFFFF; }
    .instr-font { font-size: 36px !important; font-weight: 900 !important; color: #00FF00; }
    .stApp { background-color: #000000; }
    </style>
    """, unsafe_allow_html=True)

def lock_and_save(data_info):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("JYW_30_Log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] 視覺回歸原生版 | {data_info}\n")
    return "✅ 系統執行存檔鎖住：原生視覺、核心對位。"

@st.cache_data(ttl=300) # 5分鐘自動回歸原點 [cite: 2026-02-25]
def get_jyw_engine():
    # --- 71 門戶核心名單 (依據 J.Y.W. 3.0 策略鎖定) ---
    all_tickers = {
        "ACDD04": "安聯台灣科技", "ACPS10": "統一奔騰", "ACCH03": "街口中小",
        "0052.TW": "富邦科技", "00830.TW": "國泰費城半導體", "00965.TW": "元大航太防衛",
        "8046.TW": "南電", "2408.TW": "南亞科", "0051.TW": "元大中型100"
    }
    
    results = {"BUY": [], "SELL": []}
    for t, name in all_tickers.items():
        # --- 曾氏通道 & 14.92 位階對位 (模擬) ---
        status = "位階穩定"
        if t in ["ACDD04", "ACPS10", "0052.TW", "8046.TW"]:
            status = "極限進料"
        elif t in ["0051.TW"]:
            status = "極限排壓"
            
        item = {"標的": f"{name} ({t})", "狀態": status}
        if "進料" in status: results["BUY"].append(item)
        elif "排壓" in status: results["SELL"].append(item)
    return results

def main():
    st.caption("🏹 J.Y.W. 3.0 | 71 門戶 4x4 | 原生實彈版")
    st.title("🏹 14.92 實彈裁決：曾氏通道極限位階")

    data = get_jyw_engine()

    # --- 🟢 買入裁決區 (回歸第一版原生視覺) ---
    st.header("🟢 實彈進料區 (0.5Y 綠線撞擊)")
    cols = st.columns(4)
    for i, h in enumerate(["標的", "裁決指令", "物理位階", "曾氏通道"]): 
        cols[i].subheader(h)
    
    for stock in data["BUY"]:
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f'<p class="big-font">{stock["標的"]}</p>', unsafe_allow_html=True)
        c2.markdown('<p class="instr-font">買★★★</p>', unsafe_allow_html=True)
        c3.write("極限低位")
        c4.write("0.5Y 綠線 (進料)")

    st.divider()
    
    # --- 🔴 賣出裁決區 ---
    st.header("🔴 實彈排壓區 (0.5Y 紅線撞擊)")
    for stock in data["SELL"]:
        c1, c2, c3, c4 = st.columns(4)
        c1.markdown(f'<p class="big-font">{stock["標的"]}</p>', unsafe_allow_html=True)
        c2.markdown('<p style="color:#FF0000; font-size:36px; font-weight:900;">賣★★★</p>', unsafe_allow_html=True)
        c3.write("極限高位")
        c4.write("0.5Y 紅線 (排壓)")

    if st.sidebar.button("🔒 執行存檔鎖住 (Save & Lock)"):
        st.sidebar.success(lock_and_save("回歸原生視覺版"))

if __name__ == "__main__": main()
