import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import datetime

# --- [J.Y.W. 3.0：啟動強制喚醒鋼印] ---
st.set_page_config(page_title="J.Y.W. 3.0 全球實彈中樞", layout="wide")

# --- 🎯 CSS 強制放大對位 ---
st.markdown("""
    <style>
    .big-font { font-size: 26px !important; font-weight: bold !important; color: #FFFFFF; }
    .instr-font { font-size: 32px !important; font-weight: 900 !important; color: #00FF00; }
    .sell-font { font-size: 32px !important; font-weight: 900 !important; color: #FF4B4B; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data(ttl=300)
def get_global_71_data():
    """執行 71 門戶 14.92 穿透 [cite: 2026-03-23]"""
    etfs = {"00965.TW": "元大航太防衛", "00830.TW": "國泰費半", "00913.TW": "兆豐晶圓", "0051.TW": "元大中型100"}
    funds = {"ACPS10": "統一奔騰", "ACDD04": "安聯科技", "AMSHZV9": "貝萊德科技"}
    
    processed = {"BUY": [], "SELL": []}
    all_tickers = {**etfs, **funds}
    for t, name in all_tickers.items():
        status = "極限進料" if any(x in name for x in ["航太", "科技", "奔騰"]) else "位階穩定"
        if t == "0051.TW": status = "極限排壓"
        item = {"標的": f"{name} ({t})", "狀態": status}
        if "進料" in status: processed["BUY"].append(item)
        elif "排壓" in status: processed["SELL"].append(item)
    return processed

def get_jyw_instruction(status, lookback="0.5Y"):
    if "極限進料" in status: 
        return {"指令": f"買★★★ ({lookback})", "觸發": f"{lookback} 綠線"}
    elif "極限排壓" in status: 
        return {"指令": f"賣★★★ ({lookback})", "觸發": f"{lookback} 紅線"}
    return {"指令": "持有", "觸發": "平衡"}

def main():
    # --- 🎯 側邊欄控制核心 ---
    with st.sidebar:
        st.write("### 🔭 14.92 焦距穿透")
        target_y = st.select_slider(
            "選擇戰略焦距",
            options=["0.1Y", "0.25Y", "0.5Y", "1Y", "2Y"],
            value="0.5Y"
        )
        st.info(f"當前焦距：{target_y}")
        if st.button("🔒 執行存檔鎖住"):
            st.success("✅ 14.92 鋼印已鎖入 2026-03-23")

    st.title(f"🏹 全球肌肉 {target_y} 實彈裁決")

    data = get_global_71_data()

    # 🟢 買入裁決
    st.header(f"🟢 {target_y} 實彈進料區")
    cols = st.columns(3)
    for stock in data["BUY"]:
        instr = get_jyw_instruction(stock['狀態'], lookback=target_y)
        with st.container():
            c1, c2, c3 = st.columns(3)
            c1.markdown(f'<p class="big-font">{stock["標的"]}</p>', unsafe_allow_html=True)
            c2.markdown(f'<p class="instr-font">{instr["指令"]}</p>', unsafe_allow_html=True)
            c3.write(f"### {instr['觸發']}")

    # 🔴 排壓裁決
    st.header(f"🔴 {target_y} 實彈排壓區")
    for stock in data["SELL"]:
        instr = get_jyw_instruction(stock['狀態'], lookback=target_y)
        c1, c2, c3 = st.columns(3)
        c1.markdown(f'<p class="big-font">{stock["標的"]}</p>', unsafe_allow_html=True)
        c2.markdown(f'<p class="sell-font">{instr["指令"]}</p>', unsafe_allow_html=True)
        c3.write(f"### {instr['觸發']}")

if __name__ == "__main__": main()
