import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 物理 偽裝 基因 --- [cite: 2026-03-27]
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

st.title("🚀 複利 戰場： 強制 物理 擊穿 模式")

fund_code = st.text_input("請 輸入 基金 代碼", "AC0056").upper().strip()

if fund_code:
    # 物理性 說： 只有 0000 與 0001 實體 鋼印 [cite: 2026-03-27]
    combinations = ["ya/yp010000", "ya/yp010001", "yp/yp010000", "yp/yp010001"]
    
    found = False
    for gene in combinations:
        test_url = f"https://www.moneydj.com/funddj/{gene}.djhtm?a={fund_code}"
        
        try:
            # 物理性 說： 加入 verify=False 與 HEADERS 強制 擊穿 ！！ [cite: 2026-03-27]
            resp = requests.get(test_url, headers=HEADERS, verify=False, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            name_tag = soup.find("div", {"id": "id_fundname"})
            
            if name_tag and name_tag.get_text(strip=True):
                st.success(f"🔥 物理 擊穿 成功 ！！ 鎖定： `{gene}`")
                st.write(f"基金 名稱： {name_tag.get_text(strip=True)}")
                found = True
                break
        except Exception as e:
            st.warning(f"探路 失敗： {gene}")
            continue

    if not found:
        st.error("❌ 物理 屏障 太 厚 ！！ 雲端 主機 仍 被 封鎖 中 ！！")
