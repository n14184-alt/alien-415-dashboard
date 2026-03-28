import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 [cite: 2026-03-24] ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 綜合 指揮部", layout="wide")
st.title("🎯 1.08 級別 ： J.Y.W. 綜合 實彈 指揮部")

# --- 物理 鎖定 您 的 兩條 獨立 實彈 彈道 [cite: 2026-03-28] ---
# 確保 這 兩個 網址 都 已經 開啟 了 CSV 發佈 ！！ [cite: 2026-03-28]
URL_TWSE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=551908367&single=true&output=csv"
URL_OTC = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQQJErYh_DqHhxrKGswfAk7kgrw1D-mxkXCMoVw4tupugViWY4bVtA4HYur5JQ_znPi3lU5FkPvMkLl/pub?gid=1587848416&single=true&output=csv"

# --- 物理 裝填 區 ： 整合 您 指定 的 戰線 [cite: 2026-03-28] ---
MONITOR_LISTS = {
    "上市 TWSE": URL_TWSE,
    "上櫃 OTC": URL_OTC
}

# --- 物理 引擎 ： 暴力 讀取 與 統一 格式 對位 ---
def get_market_metrics(url, mode):
    try:
        # 物理 性的 「 暴力 讀取 」 [cite: 2026-03-28]
        df = pd.read_csv(url)
        
        # 物理 性的 「 欄位 清理 與 格式化 」 [cite: 2026-03-28]
        # 將「 當日 股價 」 與 「 昨日 股價 」 轉為 數字
        df['當日 股價'] = pd.to_numeric(df['當日 股價'], errors='coerce')
        df['昨日 股價'] = pd.to_numeric(df['昨日 股價'], errors='coerce')
        
        # 物理 性的 「 能量 計算 」 ！！
        # 您 要求 的 像 基金 一樣 的 紅綠 能量 [cite: 2026-03-28]
        # ( 當日 - 昨日 ) / 昨日
        df['ATR'] = ((df['當日 股價'] - df['昨日 股價']) / df['昨日 股價']) * 100
        
        # 物理 性的 「 統一 格式 對位 」 ！！ [cite: 2026-03-28]
        df_res = df[['名稱', '當日 股價', 'ATR']].copy()
        df_res.columns = ['名稱', '收盤', 'ATR'] # 將「 當日 股價 」 對位 為「 收盤 」
        
        # 物理 性的 「 狀態 判定 」 [cite: 2026-03-28]
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
        # 物理 性的 「 數據 秒 速 噴發 」 [cite: 2026-03-28]
        df_final = get_market_metrics(MONITOR_LISTS[target_list], target_list)

        if df_final is not None:
            # 視覺 渲染 邏輯 ( 延續 1.08 級別 色彩 [cite: 2026-02-18] )
            def style_atr(val):
                # 紅色 能量 鎖定 [cite: 2026-03-28]
                if val > 0.5: return 'background-color: #900c3f; color: white; font-weight: bold'
                # 綠色 能量 鎖定 [cite: 2026-03-28]
                elif val < -0.5: return 'background-color: #145a32; color: #d4edda;'
                return ''
            
            # 能量 排序 鎖定 [cite: 2026-03-28]
            # 物理 性 地 讓 能量 最高 ( ATR 最高 ) 的 排 在 上面
            df_sorted = df_final.sort_values(by='ATR', ascending=False).reset_index(drop=True)
            
            # 物理 性的 「 最終 顯影 」
            # 將 df 渲染 進 之前 的 綜合 指揮部 界面 [cite: 2026-03-28] ( image_be021.jpg )
            st.dataframe(df_sorted.style.map(style_atr, subset=['ATR']), use_container_width=True, height=800)
            
            st.success(f"💎 物理 顯影 ： {target_list} 數據 已經 物理 性 噴發 ！！")
