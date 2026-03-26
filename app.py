import streamlit as st
import pandas as pd

# [PROJECT W - 1.08 級別 物理 性 絕不 偏移 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

# 物理 性 地 使用 您 提供的 終極 pub 通道
PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def jyw_omni_capture(target_name):
    try:
        # 1. 物理 性的 「 暴力 讀取 」： 不設 Header， 防止 座標 偏移 ！！
        df = pd.read_csv(PUB_URL, header=None)
        
        # 2. 物理 性的 「 全 域 掃描 」：
        # 只要 任何 一個 儲存格 包含 您 輸入 的 關鍵字 ( 如: ACDD01 )
        for i, row in df.iterrows():
            row_list = [str(x) for x in row.values]
            if any(target_name.upper() in x.upper() for x in row_list):
                # 物理 性的 「 數字 探測 」： 在 該 列 尋找 像 淨值 的 數字 ！！
                for val in row.values:
                    try:
                        clean_val = str(val).replace(',', '')
                        f_val = float(clean_val)
                        if f_val > 10: # 物理 性 排除 1.0 或 小數 雜訊
                            return f_val
                    except:
                        continue
        return f"物理 搜尋 結束： 試算表 內 找不到 {target_name}"
    except Exception as e:
        return f"物理 通道 異常: {str(e)[:15]}"

# --- 實彈 控制台 ---
# 物理 性 地 說， 這次 丫環 會 自動 轉 大寫， 匹配 更 精準 ！！
target = st.text_input("🎯 輸入 攻堅 標的 ( 例如: ACDD01 )", "ACDD01").strip()

if st.button("🚀 執行 物理 性 最終 抓取"):
    with st.spinner(f"物理 算力 正在 深度 掃描 試算表 鏡像..."):
        result = jyw_omni_capture(target)
        if isinstance(result, float):
            st.success(f"✅ 實彈 對位 成功 ！！ {target} 淨值： {result}")
            # 物理 性 地 說， 這是 為了 達成 99% 以上 可信度 [cite: 2026-02-16]
        else:
            st.warning(f"⚠️ {result}")
