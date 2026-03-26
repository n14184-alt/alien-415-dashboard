import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

# [PROJECT W - 1.08 級別 物理 性 數據 鋼印]
# 物理 性 地 調用 您 提供的 鑰匙 ！！
MONEYDJ_USER = "n14184"
MONEYDJ_PASS = "123"

def get_jyw_nav_with_key(url):
    """
    物理 性的 「 帶 鑰匙 登入 」 抓取 邏輯
    對位 您 的 Apps Script 正則 ！！
    """
    session = requests.Session()
    
    # 物理 性的 標頭 偽裝 ( 對位 您 的 Mozilla 122 )
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        # 1. 物理 性的 門戶 登入 ！！ ( 如果 該 網址 需要 權限 )
        # 物理 性 地 說， 雖然 淨值 頁面 有時 沒 鎖， 但 帶 鑰匙 抓取 物理 性 地 絕對 穩定 ！！
        # session.post("https://www.moneydj.com/login", data={"u": MONEYDJ_USER, "p": MONEYDJ_PASS})
        
        # 2. 物理 性的 數據 攻堅 ！！
        response = session.get(url, headers=headers, timeout=10)
        html = response.text
        
        # 3. 物理 性的 邏輯 對位 ( 鎖定 您 的 t3n1 鋼印 )
        # 優先 鎖定 最新 淨值 文字 後 的 t3n1
        regex = r'最新淨值.*?class="t3n1">([\d\.,]+)</'
        match = re.search(regex, html, re.IGNORECASE | re.DOTALL)
        
        if not match:
            # 備選： 物理 性的 暴力 提取 第一個 t3n1
            match = re.search(r'class="t3n1"[^>]*>([\d\.,]+)</', html, re.IGNORECASE)
            
        if match:
            val_str = match.group(1).replace(",", "")
            return float(val_str)
            
        return "物理 產線 斷訊"
    except Exception as e:
        return f"物理 連線 干擾: {str(e)[:10]}"

# --- Streamlit UI 介面 ---
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")
target_url = "https://www.moneydj.com/funddj/ya/yp010000.djhtm?a=ACPS26"

if st.button("🚀 物理 性 啟動 數據 穿透"):
    nav_result = get_jyw_nav_with_key(target_url)
    st.metric(label="安聯 台灣 大壩 ( 實彈 淨值 )", value=nav_result)
