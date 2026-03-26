import streamlit as st
import requests
from bs4 import BeautifulSoup

# [PROJECT W - 1.08 級別 物理 帳密 認證 鋼印]
# 物理 性 地 說， 這是 您 提供的 核心 鑰匙 ！！
USER_ID = "n14184"
USER_PW = "123"

st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def jyw_fully_authenticated_capture(fund_code):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.moneydj.com/"
    }
    
    try:
        # 1. 物理 性的 「 實彈 登入 」 ！！ ( 這是 之前 漏掉 的 關鍵 ！！ )
        # 物理 性 地 說， 必須 先 通過 這個 門， 才能 解決 image_32d438 的 斷訊 ！！
        login_url = "https://www.moneydj.com/login/login.djhtm"
        payload = {"u": USER_ID, "p": USER_PW, "isRemember": "true"}
        session.post(login_url, data=payload, headers=headers, timeout=15)
        
        # 2. 物理 性的 「 座標 攻堅 」 ！！
        # ACDD01 ( 大壩 ) / ACDD04 ( 科技 ) [cite: 2026-03-26]
        data_url = f"https://www.moneydj.com/funddj/ya/yp010001.djhtm?a={fund_code}"
        response = session.get(data_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # 物理 性 地 鎖定 您 試算表 指定 的 t3n1 標籤 ！！
            nav_element = soup.find("span", class_="t3n1")
            if nav_element:
                return nav_element.text.strip()
            return "物理 標籤 找不到 ( 頁面 可能 被 導向 )"
        return f"物理 門戶 封鎖 ({response.status_code})"
    except Exception as e:
        # 物理 性 地 針對 HTTPSConnection 進行 容錯 ！！
        return f"物理 鑰匙 失效: {str(e)[:25]}"

# --- 實彈 控制台 ---
target = st.selectbox("🎯 選擇 攻堅 標的", ["安聯台灣大壩 (ACDD01)", "安聯台灣科技 (ACDD04)"])
code = "ACDD01" if "大壩" in target else "ACDD04"

if st.button("🚀 物理 性 帶 鑰匙 真正 執行 登入 穿透"):
    with st.spinner(f"物理 算力 正在 為 {USER_ID} 執行 認證 攻堅..."):
        result = jyw_fully_authenticated_capture(code)
        if "淨值" not in str(result): # 簡單 邏輯 判斷
            st.error(f"實彈 斷訊 ！！ 報錯： {result}")
        else:
            st.success(f"實彈 對位 成功 ！！ {target} 淨值： {result}")
