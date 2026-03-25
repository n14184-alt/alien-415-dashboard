import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 實彈 最終 指揮部", layout="wide")
st.title("🎯 1.08 級別：基金 ATR 實彈 最終 指揮部")

# --- 物理 鎖定 您 的 pubhtml 彈道 [cite: 2026-03-25] ---
FINAL_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def get_jyw_final_atr():
    try:
        df = pd.read_csv(FINAL_URL)
        
        # 1. 物理 淨化： 遵照 老闆 指令， 移除 '代號'、'斜率'、'斜率(值)' [cite: 2026-03-25]
        # 只 留下 戰略 核心： 名稱、 當日、 昨日
        columns_to_keep = ['名稱', '當日股價', '昨日股價']
        df = df[columns_to_keep].copy()
        
        # 2. 物理 運算： 100% 復刻 昨天的 獵殺 算法
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        
        # 3. 物理 命名： 統一 為 唯一 動能 標籤 「 ATR 」
        df['ATR'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        # 4. 戰略 排序： ATR 強勢 優先 ( 獵人 視覺 )
        df = df.sort_values(by='ATR', ascending=False)
        
        return df
    except:
        return None

# --- 最終 視覺 渲染 ---
df_display = get_jyw_final_atr()

if df_display is not None:
    st.success("✅ 狀態： 高效 ( 試算表 實彈 最終 對位 )")
    
    # 物理 渲染： 獵人 最 滿意 的 紅綠 實彈 視覺
    def style_atr_final(val):
        if val > 0.5: # 強勢 噴 紅色
            return 'background-color: #900c3f; color: white; font-weight: bold'
        elif val < -0.5: # 低效 噴 綠色 [cite: 2026-02-18]
            return 'background-color: #145a32; color: #d4edda;'
        return ''

    # 展現 最 完美的 獵殺 介面
    st.dataframe(
        df_display.style.applymap(style_atr_final, subset=['ATR']),
        use_container_width=True,
        height=800
    )
