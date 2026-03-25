import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 最終 指揮部", layout="wide")
st.title("🎯 1.08 級別：基金 ATR 實彈 最終 指揮部")

# --- 物理 鎖定 實彈 彈道 [cite: 2026-03-25] ---
FINAL_PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def get_restored_atr():
    try:
        df = pd.read_csv(FINAL_PUB_URL)
        
        # 物理 復原 核心 欄位 ( 確保 名稱 存在 ！！ )
        # 排除 掉 代號、斜率 等 雜訊
        df = df[['名稱', '當日股價', '昨日股價']].copy()
        
        # 物理 運算 肌肉
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        
        # 100% 復刻 昨天的 算法
        df['ATR'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        # 物理 排序： ATR 強勢 優先 [cite: 2026-02-25]
        df = df.sort_values(by='ATR', ascending=False)
        return df
    except:
        return None

# --- 主 畫面 ---
df_final = get_restored_atr()

if df_final is not None:
    st.success("✅ 狀態： 高效 ( 試算表 實彈 最終 對位 )")
    
    # 物理 渲染： 獵人 最 滿意 的 紅綠 視覺 ！！
    def style_atr_restored(val):
        if val > 0.5: # 強勢 噴 紅色
            return 'background-color: #900c3f; color: white; font-weight: bold'
        elif val < -0.5: # 低效 噴 綠色 [cite: 2026-02-18]
            return 'background-color: #145a32; color: #d4edda;'
        return ''

    # 展現 您 期待 的 物理 整齊感
    st.dataframe(
        df_final.style.applymap(style_atr_restored, subset=['ATR']),
        use_container_width=True,
        height=800
    )
