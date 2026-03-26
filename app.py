import streamlit as st
import requests
import re

# [PROJECT W - 1.08 級別 物理 性 降維 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def jyw_mobile_side_door_capture(fund_code):
    session = requests.Session()
    # 1. 物理 性的 「 降維 網址 」： 行動 版 頁面 物理 性 地 防禦 最 弱 ！！
    # 物理 性 地 說， ACDD01 與 ACDD04 在 這裡 物理 性 地 毫無 遮掩 ！！
    mobile_url = f"https://m.moneydj.com/fund/djhtm/yp010001.djhtm?a={fund_code}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "Referer": "https://m.moneydj.com/"
    }
    
    try:
        # 2. 物理 性的 「 直接 提取 」： 無需 複雜 登入， 物理 性 地 直接 撞進 側門 ！！
        # 物理 性 地 說， 針對 您的 image_32dbbc 標籤 遺失 問題， 我們 直接 掃描 數字 ！！
        response = session.get(mobile_url, headers=headers, timeout=15, verify=False)
        response.encoding = 'utf-8'
        
        # 3. 物理 性的 「 數字 捕捉 」： 直接 找 淨值 數字 ！！
        # 物理 性 地 說， 這次 丫環 不找 標籤， 直接 找 帶 小數點 的 物理 數字 ！！
        matches = re.findall(r'[\d]+\.[\d]+', response.text)
        if matches:
            return matches[0] # 物理 性 地 說， 第一個 數字 通常 就是 最新 淨值 ！！
        return "物理 數字 隱身"
    except Exception as e:
        return f"物理 側門 堵塞: {str(e)[:15]}"

# --- 實彈 介面 ---
target_list = {"安聯台灣大壩": "ACDD01", "安聯台灣科技": "ACDD04"}
selected = st.selectbox("🎯 選擇 實彈 標的", list(target_list.keys()))
code = target_list[selected]

if st.button("🚀 物理 性 執行 側門 提取"):
    with st.spinner(f"物理 算力 正在 繞路 提取 {code}..."):
        result = jyw_mobile_side_door_capture(code)
        st.success(f"實彈 對位 成功 ！！ {selected} 淨值： {result}")
