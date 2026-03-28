import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 [cite: 2026-03-24] ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 綜合 指揮部", layout="wide")
st.title("🎯 1.08 級別 ： J.Y.W. 綜合 實彈 指揮部")

# --- 物理 鎖定 您的 三大 獨立 實彈 彈道 [cite: 2026-03-28] ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"
URL_TWSE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=551908367&single=true&output=csv"
URL_OTC = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQQJErYh_DqHhxrKGswfAk7kgrw1D-mxkXCMoVw4tupugViWY4bVtA4HYur5JQ_znPi3lU5FkPvMkLl/pub?gid=1587848416&single=true&output=csv"

# --- 物理 裝填 區 ： 整合 您 要求 的 三大 戰線 [cite: 2026-03-28] ---
MONITOR_LISTS = {
    "基金 (28)": URL_FUND,
    "上市 TWSE": URL_TWSE,
    "上櫃 OTC": URL_OTC
}

# --- 物理 引擎 ： 暴力 讀取 與 統一 格式 對位 ---
def get_metrics(url, mode):
    try:
        df = pd.read_csv(url)
        # 物理 性 地 統一 欄位 名稱 以 符合 舊 界面 [cite: 2026-03-28]
        if mode == "基金 (28)":
            df['收盤'] = pd.to_numeric(df['當日股價'], errors='coerce')
            df['ATR'] = ((df['收盤'] - pd.to_numeric(df['昨日股價'], errors='coerce')) / pd.to_numeric(df['昨日股價'], errors='coerce')) * 100
        else:
            # 上市 / 上櫃 物理 對位 [cite: 2026-03-28]
            df['收盤'] = pd.to_numeric(df['當日股價'], errors='coerce')
            # 物理 性 地 使用 您的 「 斜率 」 作為 能量 指標 ( 对应 ATR 視覺 位元 )
            df['ATR'] = pd.to_numeric(df['斜率'], errors='coerce').fillna(0)
            
        df_res = df[['名稱', '收盤', 'ATR']].copy()
        df_res['狀態'] = df_res['ATR'].apply(lambda x: "高效" if x > 0 else "低效")
        return df_res
    except Exception as e:
        st.error(f"❌ 物理 性 斷流 ： {mode} 失敗 ！ 原因 ： {e}")
        return None

# --- 側邊欄 視覺 鎖定 [cite: 2026-03-28] ---
st.sidebar.info("戰略 狀態 ： 保持 實彈 優先")
target_list = st.sidebar.selectbox("請 選擇 監控 公桌", list(MONITOR_LISTS.keys()))

if st.sidebar.button(f"啟動 {target_list} 買進 攻"):
    with st.spinner(f"正在 物理 校準 {target_list} 數據 ..."):
        df_final = get_metrics(MONITOR_LISTS[target_list], target_list)

        if df_final is not None:
            # 視覺 渲染 邏輯 ( 延續 1.08 級別 色彩 [cite: 2026-02-18] )
            def style_atr(val):
                if val > 0.5: return 'background-color: #900c3f; color: white; font-weight: bold'
                elif val < -0.5: return 'background-color: #145a32; color: #d4edda;'
                return ''
            
            # 能量 排序 鎖定 [cite: 2026-03-28]
            df_sorted = df_final.sort_values(by='ATR', ascending=False).reset_index(drop=True)
            st.dataframe(df_sorted.style.map(style_atr, subset=['ATR']), use_container_width=True, height=800)
            st.success(f"💎 物理 顯影 ： {target_list} 數據 已經 物理 性 噴發 ！！")
