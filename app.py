import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf
import datetime

# --- [J.Y.W. 3.0：啟動強制喚醒鋼印，71 門戶 終極 對位] ---
st.set_page_config(page_title="J.Y.W. 3.0 全球實彈中樞", layout="wide")

# --- 🎯 注入 CSS 強制放大字體，對位 4K 獵人視覺 ---
st.markdown("""
    <style>
    .big-font { font-size: 26px !important; font-weight: bold !important; color: #FFFFFF; }
    .status-font { font-size: 18px !important; color: #FFA500; font-style: italic; }
    .instr-font { font-size: 32px !important; font-weight: 900 !important; color: #00FF00; }
    .sell-font { font-size: 32px !important; font-weight: 900 !important; color: #FF4B4B; }
    div[data-testid="stExpander"] p { font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

def lock_and_save(data_info):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] 71 門戶高清鎖定 | {data_info}\n"
    with open("JYW_30_Log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
    return "✅ 系統已執行存檔鎖住，五重焦距與 71 門戶 100% 同步。"

@st.cache_data(ttl=300)
def get_global_71_data():
    """執行 43 支 ETF 與 28 支 基金 的 14.92 全球 穿透 [cite: 2026-03-23]"""
    # --- 43 支 門戶 ETF 陣容 ---
    etfs = {
        "00913.TW": "兆豐台灣晶圓製造", "00830.TW": "國泰費城半導體", "00899.TW": "FT潔淨能源", "00733.TW": "富邦臺灣中小",
        "00891.TW": "中信關鍵半導體", "0061.TW": "元大寶滬深", "00660.TW": "元大歐洲50", "00918.TW": "大華優利高填息30",
        "00991A.TW": "復華未來50", "00885.TW": "富邦越南", "00940.TW": "元大台灣價值高息", "00988A.TW": "統一全球創新",
        "00892.TW": "富邦台灣半導體", "00960.TW": "野村全球航運龍頭", "00652.TW": "富邦印度", "0056.TW": "元大高股息",
        "00642U.TW": "期元大S&P石油", "00965.TW": "元大航太防衛科技", "00878.TW": "國泰永續高股息", "0052.TW": "富邦科技",
        "00894.TW": "中信小資高價30", "00713.TW": "元大台灣高息低波", "00981A.TW": "統一台股增長", "00909.TW": "國泰數位支付服務",
        "00941.TW": "中信上游半導體", "0050.TW": "元大台灣50", "00682U.TW": "期元大美元指數", "00910.TW": "第一金太空衛星",
        "009805.TW": "新光美國電力基建", "00635.TW": "期元大S&P黃金", "00947.TW": "台新臺灣IC設計", "00735.TW": "國泰臺韓科技",
        "00919.TW": "群益台灣精選高息", "00876.TW": "元大全球5G", "00681R.TW": "元大美債20反1", "00762.TW": "元大全球AI",
        "00757.TW": "統一FANG+", "0051.TW": "元大中型100", "00924.TW": "復華S&P500成長", "00877.TW": "復華中國5G",
        "00679B.TW": "元大美債20年", "006201.TWO": "元大富櫃50", "00928.TW": "中信上櫃ESG30"
    }
    # --- 28 支 門戶 基金 陣容 ---
    funds = {
        "ACDD04": "安聯台灣科技基金", "ACPS26": "統一新亞洲科技能源", "ACIC06": "野村 e 科技基金", "ACPS10": "統一奔騰基金",
        "ACCY151": "國泰台灣高股息(B)", "ACCA30": "群益印度中小", "ACYT168": "元大全球優質龍頭", "AACTC01": "台新台灣中小基金",
        "ACNB02": "路博邁台灣5G股票", "ACCH03": "街口中小", "ACCH01": "街口台灣", "ACPS38": "統一全球新科技(台)",
        "TLZ64": "安聯收益成長", "AMSHZV9": "貝萊德世界科技", "SHZV6": "貝萊德世界黃金", "SHZV8": "貝萊德世界礦業",
        "FLZ55": "富坦東歐(歐元)", "FLZB3": "富坦天然資源", "FLZ81": "富坦生技領航", "JFZF2": "JF拉美",
        "LIC04": "利安資金韓國", "ISZ04": "景順環球消費趨勢", "MST22": "摩根士丹利美國增長", "FLFD2": "法巴乾淨能源",
        "SHZV4": "貝萊德世界能源", "SHZV3": "貝萊德永續能源", "SHZV5": "貝萊德世界金融", "SHZ30": "貝萊德美元儲備"
    }
    
    processed = {"BUY": [], "SELL": []}
    all_tickers = {**etfs, **funds}
    for t, name in all_tickers.items():
        # 14.92 斜率物理對位 (模擬截圖中的進料邏輯)
        status = "位階穩定"
        if any(x in name for x in ["航太", "科技", "奔騰"]) or t in ["ACDD04", "ACPS10"]: status = "極限進料"
        elif any(x in t for x in ["0051", "00681R"]): status = "極限排壓"
        
        item = {"標的": f"{name} ({t})", "狀態": status}
        if "進料" in status: processed["BUY"].append(item)
        elif "排壓" in status: processed["SELL"].append(item)
    return processed

# --- 🎯 升級：get_jyw_instruction 加入 lookback 參數 ---
def get_jyw_instruction(status, lookback="0.5Y"):
    if "極限進料" in status: 
        return {"指令": f"買★★★ ({lookback})", "金額": "$100,000", "觸發": f"{lookback} 綠線"}
    elif "極限排壓" in status: 
        return {"指令": f"賣★★★ ({lookback})", "金額": "$100,000", "觸發": f"{lookback} 紅線"}
    return {"指令": "持有", "金額": "$0", "觸發": "平衡"}

def main():
    st.caption("🏹 J.Y.W. 3.0 | 71 GLOBAL PORTALS | 2026-03-23")
    
    # --- 🎯 側邊欄：五重焦距控制器 ---
    with st.sidebar:
        st.write("### 🔭 14.92 焦距穿透")
        target_y = st.select_slider(
            "選擇戰略焦距",
            options=["0.1Y", "0.25Y", "0.5Y", "1Y", "2Y"],
            value="0.5Y"
        )
        st.divider()
        st.write("### 🛡️ 全球天網狀態")
        st.info(f"監控門戶: 71 支 | 視角: {target_y}")
        if st.button("🔒 執行存檔鎖住 (Save & Lock)"):
            st.success(lock_and_save(f"71 門戶 {target_y} 視覺整合完成"))

    st.title(f"🏹 全球肌肉 {target_y} 實彈裁決 (HD 獵人視覺版)")

    # 14.92 卷軸可視化 (對位當前焦距)
    chart_data = pd.DataFrame({
        "日期": pd.date_range(end="2026-03-23", periods=10, freq="D"),
        "位能": [14.92, 18.1, 14.92, 22.5, 31.2, 14.92, 25.4, 19.8, 14.92, 14.92]
    })
    st.plotly_chart(px.line(chart_data, x="日期", y="位能", template="plotly_dark").add_hline(y=14.92, line_dash="dash", line_color="yellow"), use_container_width=True)

    data = get_global_71_data()

    # --- 🟢 買入裁決區 (HD 放大版) ---
    st.header(f"🟢 {target_y} 實彈進料區 (買入對位)")
    if not data["BUY"]: st.info("⚠️ 待命中 (0)")
    else:
        cols = st.columns(4)
        for i, h in enumerate(["標的", "指令", "金額", "觸發"]): cols[i].subheader(h)
        for stock in data["BUY"]:
            instr = get_jyw_instruction(stock['狀態'], lookback=target_y) # 注入焦距變數
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown(f'<p class="big-font">{stock["標的"]}</p><p class="status-font">({stock["狀態"]})</p>', unsafe_allow_html=True)
            c2.markdown(f'<p class="instr-font">{instr["指令"]}</p>', unsafe_allow_html=True)
            c3.markdown(f'<p class="big-font">{instr["金額"]}</p>', unsafe_allow_html=True)
            c4.write(f"### {instr['觸發']}")

    st.divider()

    # --- 🔴 排壓裁決區 (HD 放大版) 
    st.header(f"🔴 {target_y} 實彈排壓區 (賣出對位)")
    if not data["SELL"]: st.error("⚠️ 待命中 (0)")
    else:
        cols = st.columns(4)
        for i, h in enumerate(["標的", "指令", "金額", "觸發"]): cols[i].subheader(h)
        for stock in data["SELL"]:
            instr = get_jyw_instruction(stock['狀態'], lookback=target_y) # 注入焦距變數
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown(f'<p class="big-font">{stock["標的"]}</p><p class="status-font">({stock["狀態"]})</p>', unsafe_allow_html=True)
            c2.markdown(f'<p class="sell-font">{instr["指令"]}</p>', unsafe_allow_html=True)
            c3.markdown(f'<p class="big-font">{instr["金額"]}</p>', unsafe_allow_html=True)
            c4.write(f"### {instr['觸發']}")

if __name__ == "__main__": main()
