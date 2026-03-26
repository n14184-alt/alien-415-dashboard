import streamlit as st
import requests
from bs4 import BeautifulSoup

# [PROJECT W - 1.08 級別 物理 帳密 壓入 鋼印]
# 物理 性 地 說， 這次 絕對 把 鑰匙 拿 在 手上 ！！ [cite: 2026-03-26]
USER_ID = "n14184"
USER_PW = "123"

st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def force_capture_with_login(fund_code):
    session = requests.Session()
    # 物理 性的 偽裝 標頭
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.moneydj.com/login"
    }
    
    try:
        # 1. 物理 性的 「 登入 壓入 」： 帶著 您的 帳密 衝 門口 ！！
        # 物理 性 地 說， 沒 這一 步， 我們 永遠 被 擋 在 image_32cd73 的 門外 ！！
        login_url = "https://www.moneydj.com/login/login.djhtm" # 物理 性 登入 接口
        login_data = {"u": USER_ID, "p": USER_PW}
        session.post(login_url, data=login_data, headers=headers, timeout=10)
        
        # 2. 物理 性的 「 座標 穿透 」： 帶著 登入 後 的 Cookie 抓 淨值 ！！
        target_url = f"https://www.moneydj.com/funddj/ya/yp010001.djhtm?a={fund_code}"
        response = session.get(target_url, headers=headers, timeout=15)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # 物理 性 地 鎖定 您 驗證 過 的 t3n1 標籤 ！！
            nav = soup.find("span", class_="t3n1")
            return nav.text.strip() if nav else "物理 標籤 偏移"
        return f"物理 門戶 封鎖 ({response.status_code})"
    except Exception as e:
        return f"物理 鑰匙 斷裂: {str(e)[:15]}"

# --- 實彈 控制台 ---
target = st.selectbox("🎯 選擇 攻堅 標的", ["安聯台灣大壩 (ACDD01)", "安聯台灣科技 (ACDD04)"])
code = "ACDD01" if "大壩" in target else "ACDD04"

if st.button("🚀 物理 性 帶 鑰匙 執行 穿透"):
    with st.spinner(f"物理 算力 攜帶 鑰匙 攻堅 {code} 中..."):
        result = force_capture_with_login(code)
        st.success(f"實彈 對位 成功 ！！ {target} 淨值： {result}")
