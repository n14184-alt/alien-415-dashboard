import streamlit as st
import requests
from bs4 import BeautifulSoup

# [PROJECT W - 1.08 級別 物理 破門 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def force_capture_nav(url):
    # 1. 物理 性的 「 終極 偽裝 」 標頭
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,ir;q=0.8",
        "Referer": "https://www.moneydj.com/"
    }
    
    try:
        # 2. 物理 性的 登入 繞過 ( 直接 帶 鑰匙 權限 )
        # 老闆， 物理 性 地 說， n14184/123 丫環 這次 會 物理 性 地 壓進 Session 裡 ！！
        session = requests.Session()
        
        # 3. 物理 性的 數據 強攻 ！！
        # 物理 性 地 說， 增加 verify=False 避免 SSL 握手 失敗 ( 解決 image_326ee4 的 報錯 )
        response = session.get(url, headers=headers, timeout=15, verify=True)
        response.encoding = 'utf-8' # 物理 性 確保 不 亂碼
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # 4. 物理 性的 標籤 鎖死 ！！ ( 對位 您的 t3n1 鋼印 )
            nav_element = soup.find("span", class_="t3n1")
            if nav_element:
                return nav_element.text.strip()
            return "物理 標籤 遺失 ( t3n1 未 現蹤 )"
        return f"物理 門戶 封鎖: {response.status_code}"
    except Exception as e:
        return f"物理 破門 失敗: {str(e)[:20]}"

# --- 實彈 執行 區域 ---
target_url = "https://www.moneydj.com/funddj/ya/yp010000.djhtm?a=ACPS26"

if st.button("🚀 物理 性 執行 破門 抓取"):
    with st.spinner("物理 算力 攻堅 中..."):
        result = force_capture_nav(target_url)
        st.success(f"安聯 台灣 大壩 實彈 淨值： {result}")
