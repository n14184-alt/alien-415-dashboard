import streamlit as st
import requests
from bs4 import BeautifulSoup

# 1.08 級別 物理性 標題 [cite: 2026-02-22]
st.markdown("<h6 style='text-align: left; font-size: 10px;'>J.Y.W. STRATEGY MARK 1.08</h6>", unsafe_allow_html=True)
st.title("🚀 複利 戰場： 真 ‧ 數據 擊穿 測試")

fund_code = st.text_input("請 輸入 基金 代碼 ( e.g., ACDD01, ACPS10 )", "").upper().strip()

if fund_code:
    # 物理性 說： 根據 領袖 0 / 1 鐵律 自動 定位 網址 [cite: 2026-03-27]
    suffix = "0000" if fund_code.endswith("0") else "1001"
    real_url = f"https://www.moneydj.com/funddj/yp/yp01{suffix}.djhtm?a={fund_code}"
    
    st.info(f"📍 物理 座標 鎖定： {real_url}")

    if st.button("啟動 實彈 抓取"):
        try:
            # 物理性 地 說： 排除 虛假 標籤， 執行 物理 穿透 ！！
            response = requests.get(real_url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 物理性 地 說： 對位 您 找到 的 id_fundname 與 t3n2 [cite: 2026-03-27]
            name_tag = soup.find("div", {"id": "id_fundname"})
            nav_tag = soup.find("td", {"class": "t3n2"})
            
            if name_tag and nav_tag:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(label="基金 中文 名稱 (id_fundname)", value=name_tag.get_text(strip=True))
                with col2:
                    st.metric(label="當日 淨值 (t3n2)", value=nav_tag.get_text(strip=True))
                st.success("✅ 物理 實彈 擊穿 成功 ！！")
            else:
                st.error("❌ 物理 性 找不到 標的 ！！ 代碼 可能 錯誤 或 尚未 掛牌 ！！")
                
        except Exception as e:
            st.error(f"物理 性 斷流： {str(e)}")
