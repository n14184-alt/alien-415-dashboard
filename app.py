import streamlit as st
import requests
from bs4 import BeautifulSoup

# 1.08 級別 物理性 標題 [cite: 2026-02-22]
st.markdown("<h6 style='text-align: left; font-size: 10px;'>J.Y.W. STRATEGY MARK 1.08</h6>", unsafe_allow_html=True)
st.title("🚀 複利 戰場： 0/1 基因 全 自動 擊穿")

# --- 物理 密鑰 --- [cite: 2026-03-27]
GAS_URL = "https://script.google.com/macros/s/AKfycbzUUcoHwhaNGMl9P6KyvUF-9cCSImO6ODv8RCsLERV_TXqgUL8NvEC7tlT-45DauvSBFg/exec"

# --- 實彈 代碼 裝填 ---
fund_code = st.text_input("請 輸入 基金 代碼 ( e.g., ACDD19, ACPS10 )", "ACDD19").upper().strip()

if fund_code:
    # 物理性 說： 核心 基因 混合 判定 邏輯 [cite: 2026-03-27]
    # 判定 1: 市場 基因 (Market) -> 0 結尾 為 境內 (0000)， 其餘 為 境外 (1001)
    market_gene = "0000" if fund_code.endswith("0") else "1001"
    
    # 判定 2: 屬性 基因 (Type) -> AC 開頭 通常 為 yp， 其餘 可 依 需求 擴充 [cite: 2026-03-27]
    type_gene = "yp" if fund_code.startswith("AC") else "yp" 
    
    # 物理性 說： 構造 最終 實彈 座標 ！！ [cite: 2026-03-27]
    target_url = f"https://www.moneydj.com/funddj/{type_gene}/{type_gene}01{market_gene}.djhtm?a={fund_code}"
    
    st.write(f"🧬 物理 基因 鎖定： `{type_gene}` | `{market_gene}`")
    st.caption(f"📍 實彈 座標： {target_url}")

    if st.button("🔥 啟動 實彈 全 鏈路 擊穿 ( A2 + C2 )"):
        try:
            # 1. 影子 算力 真 ‧ 抓取 淨值 [cite: 2026-03-27]
            resp = requests.get(target_url, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            nav_tag = soup.find("td", {"class": "t3n2"}) # 鎖定 淨值 標籤 [cite: 2026-03-27]
            
            if nav_tag:
                current_nav = nav_tag.get_text(strip=True)
                st.success(f"✅ 淨值 抓取 成功： {current_nav}")
                
                # 2. 物理性 說： 雙路 擊穿 GAS ！！ [cite: 2026-03-27]
                # 傳送 code (寫入 A2) 與 nav (寫入 C2)
                params = {"code": fund_code, "nav": current_nav}
                res_gas = requests.get(GAS_URL, params=params, timeout=15)
                
                if res_gas.status_code == 200:
                    st.success(f"🚀 實體 聯動 成功 ！！ 試算表 A2 與 C2 已 物理 性 刷新 ！！")
                else:
                    st.error("❌ 寫入 失敗， 請 檢查 GAS 代碼 是否 已 增加 nav 接收 邏輯 ！！")
            else:
                st.error("❌ 找不到 淨值 標籤， 請 檢查 代碼 物理 常數 ！！")
                
        except Exception as e:
            st.error(f"物理 性 斷流： {str(e)}")

st.divider()
st.caption("【 PROJECT W - 丫環 監控 檔案 】： 基因 混合 判定 邏輯 已 鎖定， 排除 函數 複雜 化 ！！ [cite: 2026-02-23]")
