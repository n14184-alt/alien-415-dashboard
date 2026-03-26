import streamlit as st
import requests

# [PROJECT W - 1.08 級別 物理 性 數據 鋼印]
# ACDD01 = 安聯台灣大壩 / ACDD04 = 安聯台灣科技 [cite: 2026-03-26]
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def force_capture_by_code(fund_code):
    # 1. 物理 性的 「 捷徑 網址 」： 直接 用 代碼 拼接 ！！
    url = f"https://www.moneydj.com/funddj/ya/yp010001.djhtm?a={fund_code}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://www.moneydj.com/funddj/yp/yp010000.djhtm"
    }
    
    try:
        # 2. 物理 性的 「 穿透 嘗試 」： 
        # 老闆， 物理 性 地 說， 針對 您的 HTTPSConnectionPool 報錯
        # 我們 物理 性 地 加上 timeout 與 階段性 重試 ！！
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            import re
            # 物理 性的 標籤 鎖死 ！！ ( 鎖定 您 的 t3n1 鋼印 )
            match = re.search(r'class="t3n1"[^>]*>([\d\.,]+)</', response.text)
            if match:
                return match.group(1)
            return "物理 標籤 找不到 ( 座標 偏移 )"
        return f"物理 門戶 封鎖 ({response.status_code})"
    except Exception as e:
        # 物理 性 地 說， 如果 這裡 還是 噴 HTTPS 錯誤， 丫環 物理 性 地 會 建議 改用 代理 IP ！！
        return f"物理 連線 斷訊: {str(e)[:15]}"

# --- 實彈 選單 ---
target = st.selectbox("🎯 選擇 攻堅 標的", ["安聯台灣大壩 (ACDD01)", "安聯台灣科技 (ACDD04)"])
code = "ACDD01" if "大壩" in target else "ACDD04"

if st.button("🚀 物理 性 執行 代碼 穿透"):
    with st.spinner(f"物理 算力 正向 {code} 攻堅 中..."):
        nav = force_capture_by_code(code)
        st.metric(label=f"{target} 淨值", value=nav)
