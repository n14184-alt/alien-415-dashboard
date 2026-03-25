import streamlit as st
import pandas as pd

# --- 1.08 級別 物理 鋼印 ---
st.set_page_config(page_title="J.Y.W. 3.0 基金 ATR 實彈 指揮部", layout="wide")
st.title("🏹 1.08 級別：基金 ATR 物理 實彈 運算")

# --- 物理 鎖定 實彈 彈道 ---
PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def get_purified_atr():
    try:
        df = pd.read_csv(PUB_URL)
        
        # 1. 物理 淨化： 徹底 清除 試算表 的 廢棄 欄位
        # 我們 只要 代號、名稱、淨值 (當日/昨日)
        columns_to_keep = ['代號', '名稱', '當日股價', '昨日股價']
        df = df[columns_to_keep].copy()
        
        # 2. 物理 實彈 運算： 復刻 昨天的 算法
        df['當日股價'] = pd.to_numeric(df['當日股價'], errors='coerce')
        df['昨日股價'] = pd.to_numeric(df['昨日股價'], errors='coerce')
        
        # 3. 物理 命名： 遵照 老闆 指令， 統稱為 「 ATR 」 [cite: 2026-03-25]
        df['ATR'] = ((df['當日股價'] - df['昨日股價']) / df['昨日股價']) * 100
        
        # 4. 戰略 排序： ATR 強勢 優先 [cite: 2026-02-25]
        df = df.sort_values(by='ATR', ascending=False)
        
        return df
    except:
        return None

# --- 主 畫面 ---
st.success("✅ 狀態： 高效 ( 物理 實彈 運算 中 )")

df_final = get_purified_atr()

if df_final is not None:
    # 物理 渲染： 您 滿意 的 ATR 獵殺 視覺 ！！
    def style_atr_final(val):
        if val > 0.5: # 強勢 噴 紅色
            return 'background-color: #900c3f; color: white; font-weight: bold'
        elif val < -0.5: # 低效 噴 綠色 [cite: 2026-02-18]
            return 'background-color: #145a32; color: #d4edda;'
        return ''

    # 展現 淨化 後 的 完美 介面
    st.dataframe(
        df_final.style.applymap(style_atr_final, subset=['ATR']),
        use_container_width=True,
        height=800
    )
