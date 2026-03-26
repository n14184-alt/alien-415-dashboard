import streamlit as st
import pandas as pd

# [PROJECT W - 1.08 級別 物理 性 絕不 誤 判 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 座標 反向 指揮部")

# 物理 性 地 使用 您 提供的 終極 pub 通道 ( 包含 A2 函數 刷新 )
PUB_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ9lbbB4FZm94vh_iSggV2eeQWsngZmvOf1MF5JbOH7K7Fxl02shNIS7Rj2RfdqAhkg7Q0JbAkQUJ3L/pub?output=csv"

def jyw_smart_reverse_lookup(target):
    try:
        # 1. 物理 性的 「 實時 搬運 」： 讀取 您 正在 跑 函數 的 試算表
        # 物理 性 地 說， 這次 加上 header=0 確保 欄位 對位 ！！
        df = pd.read_csv(PUB_URL)
        
        # 2. 物理 性的 「 廣域 匹配 」：
        # 針對 您 提到 的 ya/yp 或 yp/yp 變動， 丫環 不再 依賴 固定 網址 ！！
        # 我們 物理 性 地 只要 在 A 欄 (代號) 或 B 欄 (名稱) 找到 匹配， 就 提取 數據 ！！
        target = str(target).strip().upper()
        
        # 物理 性 地 搜尋 A 欄 (代號) 或 B 欄 (名稱)
        match = df[df.iloc[:, 0].astype(str).str.upper().str.contains(target) | 
                   df.iloc[:, 1].astype(str).str.upper().str.contains(target)]
        
        if not match.empty:
            # 物理 性 地 根據 您 基金.csv 的 結構 提取 座標：
            # A (0): 代號 | B (1): 名稱 | C (2): 當日 股價 ( 實彈 淨值 )
            fund_code = match.iloc[0, 0]
            fund_name = match.iloc[0, 1]
            real_nav = match.iloc[0, 2] # 這是 您的 函數 抓 下來 的 實彈 數據 ！！
            
            return {
                "code": fund_code,
                "name": fund_name,
                "nav": real_nav
            }
        return "物理 座標 偏移 ( 試算表 內 找不到 此 標的 )"
    except Exception as e:
        return f"物理 通道 斷裂 ( 請 檢查 試算表 發布 狀態 ): {str(e)[:20]}"

# --- 實彈 控制台 ---
st.write("📊 物理 性 指揮： 本 系統 透過 試算表 函數 繞過 MoneyDJ 網址 變動 限制 ！！")
search_key = st.text_input("🎯 輸入 代碼 或 名稱 ( 例如: ACDD01 或 安聯 )", "ACDD04").strip()

if st.button("🚀 執行 物理 性 反向 搜尋"):
    with st.spinner(f"正在 物理 性 檢索 您的 實彈 試算表..."):
        data = jyw_smart_reverse_lookup(search_key)
        
        if isinstance(data, dict):
            st.success(f"✅ 實彈 對位 成功 ！！")
            c1, c2, c3 = st.columns(3)
            c1.metric("物理 代號", data["code"])
            c2.metric("標的 名稱", data["name"])
            c3.metric("實時 淨值 (C 2)", data["nav"])
        else:
            st.error(f"❌ {data}")
