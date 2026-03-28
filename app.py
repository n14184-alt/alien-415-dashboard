import streamlit as st
import pandas as pd
import numpy as np

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 指揮部", layout="wide")
st.title("🎯 1.08 級別：J.Y.W. 綜合 實彈 指揮部 ( 撥 頁 整合 版 )")

# --- 物理 鎖定 雲端 抽屜 [cite: 2026-03-28] ---
# 老闆 提供的 全 撥 頁 連結 ( 整份文件 CSV 映射 )
ALL_IN_ONE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?output=csv"

# --- 物理 裝填 區： 撥 頁 自動 對位 ---
# 不再 一支 一支 寫 死 代碼， 物理 性 地 說 只要 盯著 撥 頁 ！！
MONITOR_CONFIG = {
    "ETF & 個股 ( 實時 1-2 分鐘 )": "ETF_SHEET", # 物理 性 地 讀取 ETF 頁面
    "基金 ( 淨值 結算 )": "FUND_SHEET"           # 物理 性 地 讀取 基金 頁面
}

# --- 1.08 級別 抽屜 引擎： 物理 性 映射 試算表 ---
def fetch_real_bullet_data(url):
    try:
        # 物理 性 地 讀取 試算表 CSV ( 包含 Yahoo 1-2 分鐘 實時 數據 )
        df = pd.read_csv(url)
        
        # 數據 清理 [cite: 2026-02-16]
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        
        # 物理 運算 斜率 ( ATR 實彈 變動率 )
        # 盤 中 用 盤 中， 收盤 用 收盤 ！！ [cite: 2026-03-28]
        df['ATR'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        # 格式 統一 對位
        df_res = df[['名稱', '當日股價', 'ATR']].copy()
        df_res.columns = ['名稱', '現價/淨值', '1.08 實彈 斜率 (%)']
        
        # 物理 狀態 判定
        df_res['狀態'] = df_res['1.08 實彈 斜率 (%)'].apply(lambda x: "高效" if x > 0 else "低效")
        return df_res
    except Exception as e:
        st.error(f"物理 斷電： 數據 讀取 失敗 ( {e} )")
        return None

# --- 側邊欄： 統帥 視角 ---
st.sidebar.info("戰略 狀態： 試算表 抽屜 全面 供電")
target_list = st.sidebar.selectbox("請選擇 監控 抽屜", list(MONITOR_CONFIG.keys()))

if st.sidebar.button(f"啟動 {target_list} 獵殺"):
    with st.spinner(f"正在 物理 同步 {target_list} 實彈 數據..."):
        df_final = fetch_real_bullet_data(ALL_IN_ONE_URL)

        if df_final is not None:
            # 視覺 渲染 邏輯： 物理 性 的 顏色 標記 [cite: 2026-02-18]
            def style_atr(val):
                if val > 0.5: return 'background-color: #900c3f; color: white; font-weight: bold' # 實彈 噴發
                elif val < -0.5: return 'background-color: #145a32; color: #d4edda;' # 實彈 探底
                return ''
            
            # 能量 排序 鎖定： 誰 是 當下 的 強勢 基因 ！！ [cite: 2026-03-28]
            df_sorted = df_final.sort_values(by='1.08 實彈 斜率 (%)', ascending=False).reset_index(drop=True)
            
            # 物理 顯影
            st.subheader(f"📊 {target_list} - 實時 戰報")
            st.dataframe(
                df_sorted.style.applymap(style_atr, subset=['1.08 實彈 斜率 (%)']), 
                use_container_width=True, 
                height=800
            )

# --- 預留 曾 式 通道 渲染 位置 ( 模式 A/B ) ---
st.divider()
st.caption("影子 算力 備註： 曾 式 通道 物理 繪圖 模組 隨時 準備 擊穿 ！！")
