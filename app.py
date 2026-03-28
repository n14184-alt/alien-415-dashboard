import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 [cite: 2026-03-24] ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 綜合 指揮部", layout="wide")
st.title("🎯 1.08 級別 ： J.Y.W. 綜合 實彈 指揮部")

# --- 物理 鎖定 您的 三大 實彈 彈道 [cite: 2026-03-28] ---
URL_FUND = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"
URL_TWSE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=551908367&single=true&output=csv"
URL_OTC = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQQJErYh_DqHhxrKGswfAk7kgrw1D-mxkXCMoVw4tupugViWY4bVtA4HYur5JQ_znPi3lU5FkPvMkLl/pub?gid=1587848416&single=true&output=csv"

MONITOR_LISTS = {
    "基金 (28)": URL_FUND,
    "上市 TWSE": URL_TWSE,
    "上櫃 OTC": URL_OTC
}

# --- 物理 引擎 ： 修正 欄位 命名 與 格式 暴力 對位 ---
def get_metrics(url, mode):
    try:
        df = pd.read_csv(url)
        # 物理 性 地 強制 清除 欄位 名稱 的 所有 空格 ！！ [cite: 2026-03-28]
        df.columns = [c.replace(' ', '').replace('　', '') for c in df.columns]
        
        # 物理 性的 「 實彈 對位 」 ： 統一 使用 您的 試算表 命名 「 當日股價 」 [cite: 2026-03-28]
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        
        # 物理 性的 「 能量 計算 」 ( ATR ) ！！ [cite: 2026-03-28]
        df['ATR'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        # 視覺 對位 之前的 界面 ！！ [cite: 2026-03-28] ( image_3be021.jpg )
        df_res = df[['名稱', '當日股價', 'ATR']].copy()
        df_res.columns = ['名稱', '收盤', 'ATR']
        df_res['狀態'] = df_res['ATR'].apply(lambda x: "高效" if x > 0 else "低效")
        
        return df_res
    except Exception as e:
        st.error(f"❌ 物理 性 斷流 ： {mode} 失敗 ！ 原因 ： {e}")
        return None

# --- 側邊欄 視覺 鎖定 ---
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
            
            df_sorted = df_final.sort_values(by='ATR', ascending=False).reset_index(drop=True)
            st.dataframe(df_sorted.style.map(style_atr, subset=['ATR']), use_container_width=True, height=800)
            st.success(f"💎 物理 顯影 ： {target_list} 能量 噴發 成功 ！！")
