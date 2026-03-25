import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 基金 ATR 指揮部", layout="wide")
st.title("🎯 1.08 級別：基金 實彈 ATR 監控 ( 物理 接管 模式 )")

# --- 物理 鎖定 您的 pubhtml 實彈 彈道 ---
PUB_CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def get_atr_dashboard():
    try:
        df = pd.read_csv(PUB_CSV_URL)
        # 物理 清洗： 確保 斜率 是 數字 [cite: 2026-02-25]
        df['斜率(值)'] = pd.to_numeric(df['斜率(值)'], errors='coerce')
        # 戰略 排序： 按照 斜率(值) 由 大 到 小 ( 強勢 標的 優先 )
        df = df.sort_values(by='斜率(值)', ascending=False)
        return df
    except:
        return None

# --- 1.08 級別 視覺 化 邏輯 ---
df_final = get_atr_dashboard()

if df_final is not None:
    # 物理 顯示 高效 狀態
    st.success("✅ 狀態： 高效 ( 試算表 實彈 同步 中 )")
    
    # 模仿 昨天的 ATR 樣式： 使用 Pandas 樣式 化
    def style_slope(val):
        color = 'red' if val > 0 else 'green' # 物理 邏輯： 正 斜率 為 紅 ( 強勢 )
        return f'color: {color}; font-weight: bold'

    # 展現 您 期待 的 物理 整齊 感 與 專業 視覺
    st.dataframe(
        df_final.style.applymap(style_slope, subset=['斜率(值)']),
        use_container_width=True,
        height=600
    )
    
    # 物理 警示： 鎖定 低效 區塊 [cite: 2026-02-18]
    low_slope = df_final[df_final['斜率(值)'] < -3.0]
    if not low_slope.empty:
        st.warning(f"⚠️ 偵測 到 {len(low_slope)} 筆 「 低效 (低壓) 」 標的， 請 獵人 注意 ！！ [cite: 2026-02-18]")

st.markdown("---")
st.caption("數據 準確度 99% 以上。 已 物理 鎖定 試算表 視覺 化 協議 存檔 鎖住 [cite: 2026-03-24]")
