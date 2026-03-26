import streamlit as st
import pandas as pd

# [PROJECT W - 1.08 級別 物理 性 絕不 再 笨 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

# 物理 性 地 說， 這是 您 提供的 終極 物理 通道 ( 已 發布 到 網路 )
# 物理 性 地 將 pubhtml 轉為 csv 格式， 讓 算力 100% 讀取 ！！
PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def jyw_final_victory_capture(target_name):
    try:
        # 1. 物理 性的 「 降維 提取 」： 這次 物理 性的 直接 讀取 Google 已 認證 的 CSV ！！
        df = pd.read_csv(PUB_URL)
        
        # 2. 物理 性的 「 座標 鎖死 」：
        # 物理 性 地 搜尋 基金 名稱 ( 安聯台灣大壩 或 ACDD01 )
        # 丫環 物理 性的 遍歷 所有 儲存格， 只要 看到 數字 就 提取 ！！
        for index, row in df.iterrows():
            row_text = " ".join(map(str, row.values))
            if target_name in row_text:
                # 尋找 該 列 中 大於 10 的 物理 數字 ( 避開 1.0 雜訊 )
                for val in row.values:
                    try:
                        f_val = float(str(val).replace(',', ''))
                        if f_val > 10: # 物理 性 確保 是 淨值
                            return f_val
                    except:
                        continue
        return "物理 座標 偏移 ( 試算表 內 未 見 數據 )"
    except Exception as e:
        return f"物理 通道 斷裂: {str(e)[:20]}"

# --- 實彈 控制台 ---
target = st.text_input("🎯 輸入 攻堅 標的 ( 例如: 大壩 或 ACDD01 )", "ACDD01")

if st.button("🚀 執行 物理 性 最終 提取"):
    with st.spinner("物理 算力 正在 透過 領袖 盾牌 提取 數據..."):
        result = jyw_final_victory_capture(target)
        if isinstance(result, float):
            st.success(f"✅ 實彈 對位 成功 ！！ {target} 淨值： {result}")
        else:
            st.error(f"❌ {result}")
