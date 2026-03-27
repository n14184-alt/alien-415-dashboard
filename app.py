import streamlit as st
import requests

# 1.08 級別 物理性 標題 [cite: 2026-02-22]
st.markdown("<h6 style='text-align: left; font-size: 10px;'>J.Y.W. STRATEGY MARK 1.08</h6>", unsafe_allow_html=True)
st.title("🚀 複利 戰場： 實彈 寫入 測試器")

# --- 物理 鑰匙 配置 ---
# 物理性 說： 請 貼入 您 部署 後 取得 的 那 串 Web App URL ！！
GAS_URL = st.text_input("請 貼入 您的 GAS 網址 (Web App URL)", "https://script.google.com/macros/s/...")

# --- 實彈 代碼 裝填 ---
fund_code = st.text_input("請 輸入 基金 代碼 ( e.g., ACDD01 )", "").upper().strip()

if fund_code and GAS_URL:
    # 物理性 說： 根據 領袖 0 / 1 鐵律 顯示 預期 市場 [cite: 2026-03-27]
    market = "境內 (0)" if fund_code.endswith("0") else "境外 (1)"
    st.write(f"物理 判定 市場： **{market}**")

    if st.button("🔥 執行 實彈 寫入 A2"):
        try:
            # 物理性 地 說： 穿透 雲端， 擊穿 試算表 A2 ！！
            response = requests.get(GAS_URL, params={"code": fund_code}, timeout=10)
            
            if response.status_code == 200:
                st.success(f"✅ 物理 擊穿 成功 ！！ 試算表 回傳： {response.text}")
                st.info("💡 請 現在 物理 性 地 檢查 您的 試算表 A2 與 C2 淨值 ！！")
            else:
                st.error(f"❌ 物理 性 斷流： 狀態 碼 {response.status_code}")
                
        except Exception as e:
            st.error(f"物理 性 傳輸 失敗： {str(e)}")

# --- 物理 性的 存檔 鎖住 標註 ---
st.divider()
st.caption("【 PROJECT W - 丫環 監控 檔案 】： 實彈 寫入 邏輯 已 鎖定， 排除 虛假 模擬 ！！")
