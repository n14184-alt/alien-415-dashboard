import streamlit as st
import requests
from bs4 import BeautifulSoup
import time

# 1.08 級別 物理性 標題 [cite: 2026-02-22]
st.markdown("<h6 style='text-align: left; font-size: 10px;'>J.Y.W. STRATEGY MARK 1.08</h6>", unsafe_allow_html=True)
st.title("🚀 複利 戰場： 真 ‧ 實彈 聯動 測試器")

# --- 物理 鑰匙 配置 ---
# 物理性 說： 請 貼入 您 部署 後 取得 的 那 串 AKfycbz... 網址 ！！ [cite: 2026-03-27]
GAS_URL = st.text_input("請 貼入 您的 GAS 網址 (Web App URL)", "https://script.google.com/macros/s/AKfycbzUUcoHwhaNGMl9P6KyvUF-9cCSImO6ODv8RCsLERV_TXqgUL8NvEC7tlT-45DauvSBFg/exec")

# --- 實彈 代碼 裝填 ---
fund_code = st.text_input("請 輸入 基金 代碼 ( e.g., ACDD19 )", "ACDD19").upper().strip()

if fund_code and GAS_URL:
    # 物理性 地 說： 根據 領袖 的 0 / 1 鐵律， 判定 市場 基因 [cite: 2026-03-27]
    suffix = "0000" if fund_code.endswith("0") else "1001"
    # 對位 您的 yp010000 (境內) 或 yp011001 (境外) [cite: 2026-03-27]
    real_mdj_url = f"https://www.moneydj.com/funddj/yp/yp01{suffix}.djhtm?a={fund_code}"
    
    st.info(f"📍 影子 算力 已 鎖定 MoneyDJ 座標： {real_mdj_url}")

    # 兩 個 物理性 按鈕， 分別 執行 介面 抓取 與 實體 寫入
    col_run, col_write = st.columns(2)

    with col_run:
        if st.button("啟動 物理 真 ‧ 抓取 (介面 顯示)"):
            try:
                # 物理性 地 說： BeautifulSoup 真 ‧ 擊穿 網頁 標籤 ！！ [cite: 2026-03-27]
                response_mdj = requests.get(real_mdj_url, timeout=10)
                soup = BeautifulSoup(response_mdj.text, 'html.parser')
                
                # 對位 您的 id_fundname 與 td.t3n2 [cite: 2026-03-27]
                name_tag = soup.find("div", {"id": "id_fundname"})
                nav_tag = soup.find("td", {"class": "t3n2"})
                
                if name_tag and nav_tag:
                    st.success("✅ 介面 真 ‧ 擊穿 成功 ！！")
                    st.metric(label=f"基金 中文 名稱 ({fund_code})", value=name_tag.get_text(strip=True))
                    st.metric(label="當日 淨值 (C2 聯動 目標)", value=nav_tag.get_text(strip=True))
                else:
                    st.error("❌ 物理 性 找不到 標的 (代碼 錯誤) ！！")
                    
            except Exception as e:
                st.error(f"物理 性 斷流： {str(e)}")

    with col_write:
        if st.button("🔥 執行 實彈 真 ‧ 寫入 A2 (跨 平臺)"):
            try:
                # 物理性 地 說： 穿透 雲端， 擊穿 試算表 A2 ！！ [cite: 2026-03-27]
                # 不需要 帳 密， 因為 所有人 權限 隧道 已經 鑿通 ！！
                response_gas = requests.get(GAS_URL, params={"code": fund_code}, timeout=15)
                
                if response_gas.status_code == 200:
                    st.success(f"✅ 試算表 A2 真 ‧ 擊穿 成功 ！！ 回傳： {response_gas.text}")
                    st.info(f"💡 請 現在 物理 性 地 檢查 您的 試算表 A2 與 C2 (對位 ACDD19) ！！")
                else:
                    st.error(f"❌ 物理 性 寫入 失敗： 狀態 碼 {response_gas.status_code}")
                    
            except Exception as e:
                st.error(f"物理 性 寫入 失敗 (權限 或 網址 錯誤) ！！")

# --- 物理 性的 存檔 鎖住 標註 ---
st.divider()
st.caption("【 PROJECT W - 丫環 監控 檔案 】： 實彈 真 ‧ 寫入 與 BeautifulSoup 真 ‧ 抓取 邏輯 已 鎖定， 排除 虛假 模擬 ！！")
