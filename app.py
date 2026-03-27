import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 物理 鑰匙 ---
GAS_URL = "https://script.google.com/macros/s/AKfycbzUUcoHwhaNGMl9P6KyvUF-9cCSImO6ODv8RCsLERV_TXqgUL8NvEC7tlT-45DauvSBFg/exec"

st.title("🚀 複利 戰場： 0000 / 0001 鋼印 擊穿")

fund_code = st.text_input("請 輸入 基金 代碼", "AC0056").upper().strip()

if fund_code:
    # 物理性 說： 遵照 領袖 指示， 只 使用 0000 與 0001 物理 常數 ！！ [cite: 2026-03-27]
    combinations = [
        "ya/yp010000", # 物理 判定 1
        "ya/yp010001", # 物理 判定 2
        "yp/yp010000", # 物理 判定 3
        "yp/yp010001"  # 物理 判定 4
    ]
    
    found = False
    for gene in combinations:
        test_url = f"https://www.moneydj.com/funddj/{gene}.djhtm?a={fund_code}"
        
        # 物理性 地 說： 影子 算力 執行 物理 探路 ！！ [cite: 2026-03-27]
        try:
            resp = requests.get(test_url, timeout=5)
            soup = BeautifulSoup(resp.text, 'html.parser')
            name_tag = soup.find("div", {"id": "id_fundname"})
            
            # 物理性 說： 必須 真的 抓到 名字 才 算 擊穿 ！！
            if name_tag and name_tag.get_text(strip=True):
                st.success(f"✅ 物理 鋼印 擊穿 成功 ！！ 鎖定： `{gene}`")
                st.info(f"📍 最終 實彈 座標： {test_url}")
                
                # 抓取 淨值 並 執行 A2+C2 實體 聯動
                nav_tag = soup.find("td", {"class": "t3n2"})
                if nav_tag:
                    current_nav = nav_tag.get_text(strip=True)
                    st.metric(label="目前 淨值 (C2)", value=current_nav)
                    
                    if st.button("🔥 執行 實彈 真 ‧ 寫入 (A2+C2)"):
                        requests.get(GAS_URL, params={"code": fund_code, "nav": current_nav})
                        st.success("🚀 數據 已 物理 性 灌入 A2 與 C2 ！！")
                found = True
                break 
        except:
            continue

    if not found:
        st.error("❌ 0000/0001 組合 全數 失效， 請 檢查 代碼 ！！")
