import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 終極 指揮部", layout="wide")
st.title("🎯 1.08 級別：J.Y.W. 3.0 全 戰場 整合 ( 撥 頁 修復 版 )")

# --- 物理 鎖定 實彈 網址 [cite: 2026-03-28] ---
# 關鍵 修復： 物理 性 地 確保 每一條 網址 都是 直接 輸出 CSV 格式 ！！
URL_MAP = {
    "ETF & 個股 ( 上市 )": "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=0&output=csv",
    "ETF & 個股 ( 上 櫃 )": "https://docs.google.com/spreadsheets/d/e/2PACX-1vR9oPfIYlq-RfIqdmmWbcXbjTFCmhtdoCaQfW8t7oI5jg0t6DZijm4r0LZjZLTEJTBbHGJ-EtmprQes/pub?gid=1508249822&output=csv",
    "基金 ( 淨值 結算 )": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"
}

# --- 1.08 級別 抽屜 引擎： 物理 性 映射 試算表 ---
def fetch_real_bullet_data(url):
    try:
        # 物理 性 地 強制 用 CSV 引擎 讀取
        df = pd.read_csv(url, on_bad_lines='skip') 
        
        # 物理 性 地 清洗 數據， 排除 所有的 雜訊 [cite: 2026-02-16]
        # 確保 您的 「 名稱 」、 「 當日 股價 」 欄 位 物理 性 地 對位 ！！
        df.columns = [c.strip() for c in df.columns] # 物理 移除 空格
        
        needed_cols = ['名稱', '當日股價', '昨日股價']
        if not all(col in df.columns for col in needed_cols):
            st.error(f"物理 斷電： 試算表 欄 位 不符 ！！ 找 不到 {needed_cols}")
            return None

        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        df = df.dropna(subset=['名稱', '當日股價', '昨日股價'])
        
        # 物理 運算 1.08 斜率
        df['1.08 實彈 斜率 (%)'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        df_res = df[['名稱', '當日股價', '1.08 實彈 斜率 (%)']].copy()
        df_res.columns = ['名稱', '現價/淨值', '1.08 實彈 斜率 (%)']
        df_res['狀態'] = df_res['1.08 實彈 斜率 (%)'].apply(lambda x: "高效" if x > 0 else "低效")
        return df_res
    except Exception as e:
        st.error(f"物理 異常： {e}")
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
            
            df_sorted = df_final.sort_values(by='1.08 實彈 斜率 (%)', ascending=False).reset_index(drop=True)
            st.subheader(f"📊 {target_list} - 實戰 數據")
            st.dataframe(df_sorted.style.applymap(style_atr, subset=['1.08 實彈 斜率 (%)']), use_container_width=True, height=800)
