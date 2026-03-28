import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 終極 指揮部", layout="wide")
st.title("🎯 1.08 級別：J.Y.W. 3.0 全 戰場 整合 ( 網址 歸位 修復 版 )")

# --- 物理 鎖定 實彈 網址 [cite: 2026-03-28] ---
# 修正 關鍵： 物理 性 地 移除 多餘 參數， 確保 每個 網址 物理 性 獨立 ！！
URL_MAP = {
    "ETF & 個股 ( 上市 )": "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=0&output=csv",
    "基金 ( 淨值 結算 )": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"
}

def fetch_real_bullet_data(url):
    try:
        # 物理 性 地 強制 讀取 CSV， 排除 所有的 400 報錯 [cite: 2026-03-28]
        df = pd.read_csv(url)
        
        # 物理 性 地 確保 欄 位 對位 [cite: 2026-03-28] ( image_1d5f86.jpg )
        df.columns = [c.strip() for c in df.columns]
        
        # 物理 性 地 轉換 數據 並 排除 雜訊 [cite: 2026-02-16]
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        df = df.dropna(subset=['名稱', '當日股價', '昨日股價'])
        
        # 1.08 級別 斜率 運算
        df['1.08 實彈 斜率 (%)'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        df_res = df[['名稱', '當日股價', '1.08 實彈 斜率 (%)']].copy()
        df_res.columns = ['名稱', '現價/淨值', '1.08 實彈 斜率 (%)']
        df_res['狀態'] = df_res['1.08 實彈 斜率 (%)'].apply(lambda x: "高效" if x > 0.5 else "低效")
        return df_res
    except Exception as e:
        # 物理 性 地 攔截 所有的 異常
        st.error(f"物理 異常： 無法 讀取 分頁 數據， 請 檢查 發佈 設置 ！！ ( {e} )")
        return None

# --- 側邊欄 與 渲染 ( 邏輯 物理 性 鎖死 ) ---
target_list = st.sidebar.selectbox("請選擇 監控 抽屜", list(URL_MAP.keys()))
if st.sidebar.button(f"啟動 {target_list} 獵殺"):
    df_final = fetch_real_bullet_data(URL_MAP[target_list])
    if df_final is not None:
        df_sorted = df_final.sort_values(by='1.08 實彈 斜率 (%)', ascending=False).reset_index(drop=True)
        st.subheader(f"📊 {target_list} - 歸位 戰報")
        st.dataframe(df_sorted, use_container_width=True, height=600)
