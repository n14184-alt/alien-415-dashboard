import requests
from bs4 import BeautifulSoup
import streamlit as st

def fetch_fund_nav_by_isin_v1(isin):
    """
    [方案一]： 物理 性 網頁 原始碼 狙擊 ！！ ( 0 瀏覽器 依賴 )
    """
    url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin}"
    # 物理 性的 領袖 偽裝， 避免 被 伺服器 識破
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            # 物理 性 地 鎖定 MoneyDJ 核心 淨值 標籤 t3n2
            nav_element = soup.find("span", class_="t3n2")
            if nav_element:
                return nav_element.text.strip()
        return "方案一 穿透 失敗"
    except Exception as e:
        return f"連線 異常: {str(e)[:15]}"

# 實彈 顯示：
# st.write(f"安聯 淨值: {fetch_fund_nav_by_isin_v1('TW000T3604Y3')}")
