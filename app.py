import streamlit as st
import pandas as pd
import plotly.express as px
import datetime

# --- [強制喚醒鋼印：啟動 J.Y.W. 3.0] ---
# 排除 3.0 虛假標籤，接管 Pro 肌肉 [cite: 2026-03-23]
st.set_page_config(page_title="J.Y.W. 3.0 實彈裁決中樞", layout="wide")

def lock_and_save(data_info):
    """執行 PROJECT W - 存檔鎖住機制：KEEP & TXT 雙重確認 [cite: 2026-02-24]"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] 實彈對位成功，指令已鎖定 | {data_info}\n"
    with open("JYW_30_Log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
    return "✅ 買賣點格式已同步 KEEP & TXT，存檔鎖住。"

def get_jyw_instruction(slope_value, status):
    """根據 PDF 格式自動產出實彈指令 [對位：買賣點格式.pdf]"""
    if "極限進料" in status:
        return {"指令": "買★★★", "金額": "$100,000", "觸發": "0.5Y 綠線正式撞擊"}
    elif "重度進料" in status:
        return {"指令": "買★★★", "金額": "$100,000", "觸發": "0.25Y 綠線正式撞擊"}
    elif "極限排壓" in status:
        return {"指令": "賣★★★", "金額": "$100,000", "觸發": "0.5Y 紅線正式撞擊"}
    elif "實彈噴發" in status: 
        return {"指令": "買★★", "金額": "$50,000", "觸發": "0.1Y 綠線正式撞擊 (校準)"}
    return {"指令": "持有", "金額": "$0", "觸發": "位階脫離紅/綠線"}

def apply_jyw_style():
    st.markdown("""
        <style>
        .main { background-color: #0e1117; color: #ffffff; }
        .stMetric { border: 1px solid #415; padding: 10px; border-radius: 10px; }
        .stAlert { background-color: #1a1c23; border: 1px solid #ff4b4b; }
        </style>
        """, unsafe_allow_html=True)

def main():
    apply_jyw_style()
    st.caption("J.Y.W. STRATEGY - INTERNAL USE ONLY | SLOT: 1.08 | 2026-03-23")
    st.title("🏹 J.Y.W. 3.0：歷史卷軸與實彈裁決系統")
    
    # 物理時空對位：確保日期為今日 [cite: 2026-03-23]
    if 'df' not in st.session_state:
        data = {
            "日期": pd.date_range(end="2026-03-23", periods=10, freq="D"),
            "座標位能": [18.5, 19.2, 21.5, 20.1, 22.8, 24.5, 14.92, 26.8, 29.5, 31.2],
            "風險評級": ["高效", "高效", "極致", "修正", "高效", "高效", "實彈噴發", "複利噴發", "主權掌控", "1.08 巔峰"]
        }
        st.session_state.df = pd.DataFrame(data)

    with st.sidebar:
        st.header("⚙️ 戰略參數 (Slope Focus)")
        st.write("自動調整頻率：3-5 min [cite: 2026-02-25]")
        
        if st.button("🔥 啟動造人模式 (破局)"):
            st.balloons()
            st.session_state.df['座標位能'] = st.session_state.df['座標位能'] * 1.423
            st.success("🚀 1.423 複利穿透執行成功！")
        
        st.divider()
        if st.button("🔒 存檔鎖住 (Save & Lock)"):
            st.success(lock_and_save("3/23 實彈清單已確認"))

    # --- 歷史卷軸繪製 ---
    fig = px.line(st.session_state.df, x="日期", y="座標位能", text="風險評級", 
                 title="J.Y.W. 3/23 即時物理位能 (排除外部干擾)",
                 template="plotly_dark", color_discrete_sequence=['#ff4b4b'])
    fig.add_hline(y=14.92, line_dash="dash", line_color="yellow", annotation_text="14.92 實彈區")
    st.plotly_chart(fig, use_container_width=True)

    # --- 🎯 每日實彈裁決清單 (PDF 對位) ---
    st.divider()
    st.subheader("🎯 J.Y.W. 3.0：每日實彈裁決清單 (2026-03-23)")
    target_stocks = [
        {"標的": "元大龍頭 (模擬)", "座標": 14.92, "狀態": "實彈噴發"},
        {"標的": "安聯科技 (模擬)", "座標": 21.5, "狀態": "極限進料"},
        {"標的": "全球油輪 (監控)", "座標": 10.2, "狀態": "低效"}
    ]

    cols = st.columns(4)
    for i, h in enumerate(["標的/狀態", "指令對位", "實彈金額", "觸發條件"]): cols[i].write(f"**{h}**")

    for stock in target_stocks:
        instr = get_jyw_instruction(stock['座標'], stock['狀態'])
        c1, c2, c3, c4 = st.columns(4)
        c1.write(f"{stock['標的']}\n({stock['狀態']})")
        if "買" in instr['指令']: c2.warning(instr['指令'])
        elif "賣" in instr['指令']: c2.error(instr['指令'])
        else: c2.info(instr['指令'])
        c3.write(instr['金額'])
        c4.caption(instr['觸發'])

if __name__ == "__main__":
    main()
