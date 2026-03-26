import requests
from bs4 import BeautifulSoup
import streamlit as st

def fetch_fund_nav_by_isin(isin):
    # 物理 性的 「 數據 門戶 」
    url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin}"
    
    # 物理 性的 「 偽裝 鋼印 」
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        # 物理 性 地 直接 撞擊 數據 牆
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 物理 性 地 摳 出 淨值 ( MoneyDJ 唯一 標籤 t3n2 )
        nav = soup.find("span", class_="t3n2").text.strip()
        return nav
    except:
        return "連線 中..."

# 物理 性 地 讓 數據 在 指揮部 歸位 ！！
st.write(f"安聯 台灣 科技 (ISIN: TW000T3604Y3) 淨值: {fetch_fund_nav_by_isin('TW000T3604Y3')}")
