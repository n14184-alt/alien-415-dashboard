import streamlit as st
import pandas as pd

# [PROJECT W - 1.08 級別 物理 性 座標 搜尋 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 座標 搜尋 器")

# 物理 性的 說， 丫環 這次 直接 鎖定 您 提供的 物理 網址
# ( 根據 image_31f77e 的 ID， 使用 pub 模式 確保 函數 刷新 )
PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def jyw_reverse_lookup(target_code):
    try:
        # 1. 物理 性的 「 數據 鏡像 」： 抓取 您 含有 函數 的 試算表
        df = pd.read_csv(PUB_URL)
        
        # 物理 性 地 說， 統一 清除 欄位 空格， 確保 A 欄 (代號) 絕對 匹配
        df.columns = [str(c).strip() for c in df.columns]
        
        # 2. 物理 性的 「 反向 搜尋 」： 
        # 針對 A 欄 (代號) 進行 物理 性 鎖定
        # 只要 代號 ( 如: ACDD01 ) 對位 成功， 物理 性 地 提取 同一 列 的 C 欄 (當日股價)
        match = df[df.iloc[:, 0].astype(str).str.contains(target_code, case=False, na=False)]
        
        if not match.empty:
            # 根據 您的 指揮： A(0)=代號, B(1)=名稱, C(2)=當日股價
            nav = match.iloc[0, 2] # 物理 性 提取 C 欄 ！！
            name = match.iloc[0, 1] # 物理 性 提取 B 欄 ！！
            return name, nav
        return None, "物理 代號 未 於 座標 內 尋獲"
    except Exception as e:
        return None, f"物理 通道 阻塞: {str(e)[:15]}"

# --- 實彈 控制台 ---
st.info("💡 物理 提示： 只要 試算表 內 的 A2 函數 在 跑， 這裡 就是 實時 的 ！！")
code_input = st.text_input("🎯 請 輸入 攻堅 代碼 (例如: ACDD01 或 ACDD04)", "ACDD04").strip()

if st.button("🚀 執行 物理 反向 搜尋"):
    with st.spinner(f"正在 物理 性 鎖定 {code_input} 的 C2 座標..."):
        name, result = jyw_reverse_lookup(code_input)
        if name:
            st.success(f"✅ 實彈 對位 成功 ！！")
            col1, col2 = st.columns(2)
            col1.metric("標的 名稱", name)
            col2.metric("最新 淨值 (C 欄)", result)
        else:
            st.error(f"❌ {result}")
