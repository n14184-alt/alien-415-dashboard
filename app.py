import streamlit as st
import requests
import urllib3

# [PROJECT W - 1.08 級別 物理 憑證 破門 鋼印]
# 物理 性 地 禁用 安全 警告， 確保 畫面 乾淨 ！！
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

USER_ID = "n14184"
USER_PW = "123"

st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def jyw_brute_force_capture(fund_code):
    session = requests.Session()
    # 物理 性的 頂級 偽裝
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.moneydj.com/"
    }
    
    try:
        # 1. 物理 性的 「 暴力 登入 」： 
        # 物理 性 地 說， 加上 verify=False 解決 image_32d7ff 的 憑證 報錯 ！！
        login_url = "https://www.moneydj.com/login/login.djhtm"
        payload = {"u": USER_ID, "p": USER_PW}
        session.post(login_url, data=payload, headers=headers, timeout=15, verify=False)
        
        # 2. 物理 性的 「 座標 提取 」：
        # ACDD01 ( 大壩 ) / ACDD04 ( 科技 ) [cite: 2026-03-26]
        data_url = f"https://www.moneydj.com/funddj/ya/yp010001.djhtm?a={fund_code}"
        response = session.get(data_url, headers=headers, timeout=20, verify=False)
        
        if response.status_code == 200:
            import re
            # 物理 性 地 鎖定 實彈 標籤 t3n1 ！！
            match = re.search(r'class="t3n1"[^>]*>([\d\.,]+)</', response.text)
            if match:
                return match.group(1)
            return "物理 標籤 遺失"
        return f"物理 門戶 封鎖: {response.status_code}"
    except Exception as e:
        # 物理 性 地 捕捉 最終 異常
        return f"物理 認證 崩潰: {str(e)[:30]}"

# --- 實彈 控制台 ---
target = st.selectbox("🎯 選擇 攻堅 標的", ["安聯台灣大壩 (ACDD01)", "安聯台灣科技 (ACDD04)"])
code = "ACDD01" if "大壩" in target else "ACDD04"

if st.button("🚀 物理 性 暴力 破門 提取"):
    with st.spinner(f"物理 算力 正在 為 {USER_ID} 強行 破除 憑證 封鎖..."):
        result = jyw_brute_force_capture(code)
        if "崩潰" in str(result) or "封鎖" in str(result):
            st.error(f"實彈 斷務 ！！ 物理 報錯： {result}")
        else:
            st.success(f"實彈 對位 成功 ！！ {target} 淨值： {result}")
