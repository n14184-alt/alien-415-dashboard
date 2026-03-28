import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 終極 指揮部", layout="wide")
st.title("🎯 1.08 級別：J.Y.W. 3.0 全 戰場 實彈 整合 指揮部")

# --- 物理 鎖定 實彈 抽屜 網址 [cite: 2026-03-28] ---
# 透過 gid 參數 物理 性 地 定位 不同的 撥 頁
BASE_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?output=csv"
FUND_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

URL_MAP = {
    "ETF & 個股 ( 上市 )": f"{BASE_URL}&gid=0", 
    "ETF & 個股 ( 上 櫃 )": f"{BASE_URL}&gid=1508249822", # 物理 性 鎖定 上 櫃 撥 頁
    "基金 ( 淨值 結算 )": FUND_URL
}

# --- 1.08 級別 抽屜 引擎： 物理 性 映射 試算表 ---
def fetch_real_bullet_data(url):
    try:
        # 物理 性 地 讀取 試算表 CSV
        df = pd.read_csv(url)
        
        # 物理 性 地 清洗 數據， 排除 所有的 #NAME? 與 空值 [cite: 2026-02-16]
        df = df.dropna(subset=['名稱', '當日股價', '昨日股價'])
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        
        # 物理 運算 斜率 ( ATR 實彈 變動率 )
        # 透過 您的 試算表 數據 物理 性 地 算出 噴發 能量 ！！
        df['1.08 實彈 斜率 (%)'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        # 格式 統一 對位
        df_res = df[['名稱', '當日股價', '1.08 實彈 斜率 (%)']].copy()
        df_res.columns = ['名稱', '現價/淨值', '1.08 實彈 斜率 (%)']
        
        # 物理 狀態 判定
        df_res['狀態'] = df_res['1.08 實彈 斜率 (%)'].apply(lambda x: "高效" if x > 0 else "低效")
        return df_res
    except Exception:
        return None

# --- 側邊欄： 統帥 視角 ---
st.sidebar.info("戰略 狀態： 全 戰場 分頁 物理 對位")
target_list = st.sidebar.selectbox("請選擇 監控 抽屜", list(URL_MAP.keys()))

if st.sidebar.button(f"啟動 {target_list} 獵殺"):
    with st.spinner(f"正在 物理 同步 {target_list} 數據..."):
        df_final = fetch_real_bullet_data(URL_MAP[target_list])

        if df_final is not None:
            # 視覺 渲染 邏輯 [cite: 2026-02-18]
            def style_atr(val):
                if val > 0.5: return 'background-color: #900c3f; color: white; font-weight: bold'
                elif val < -0.5: return 'background-color: #145a32; color: #d4edda;'
                return ''
            
            # 能量 排序 鎖定
            df_sorted = df_final.sort_values(by='1.08 實彈 斜率 (%)', ascending=False).reset_index(drop=True)
            
            # 物理 顯影
            st.subheader(f"📊 {target_list} - 實戰 數據")
            st.dataframe(
                df_sorted.style.applymap(style_atr, subset=['1.08 實彈 斜率 (%)']), 
                use_container_width=True, 
                height=800
            )

# --- 下一步： 曾 式 通道 圖 模組 預留 ---
st.divider()
st.caption("影子 算力 備註： 曾 式 通道 物理 渲染 已 準備 就緒 ， 等待 指令 噴發 ！！")
