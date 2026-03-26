import requests
from bs4 import BeautifulSoup
import streamlit as st

# [PROJECT W - 1.08 級別 數據 接口 鋼印 存檔 鎖住]
# 物理 性 地 棄用 瀏覽器， 直接 穿透 數據 源頭 ！！

def fetch_fund_nav_by_isin(isin_code):
    """
    物理 性 地 透過 ISIN 碼 直接 向 MoneyDJ 請求 原始 網頁， 0 瀏覽器 負載 ！！
    """
    # 物理 性的 偽裝 標頭， 讓 伺服器 以為 是 領袖 親自 到訪
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    # 物理 性的 鑰匙 接口
    url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin_code}"
    
    try:
        # 物理 性 地 直接 拿 取 網頁 原始碼
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 物理 性的 密室 提取： 鎖定 MoneyDJ 淨值 專用 標籤 t3n2
            nav_element = soup.find("span", class_="t3n2")
            
            if nav_element:
                nav_value = nav_element.text.strip()
                return nav_value
            else:
                return "物理 密室 鎖定 (找不到標籤)"
        else:
            return f"源頭 拒絕 (錯誤碼:{response.status_code})"
            
    except Exception as e:
        return f"連線 崩潰: {str(e)[:20]}"

# --- 1.08 級別 實彈 顯示 ---
# isin_keys = ["TW000T3604Y3", "TW000T0910ACY7"]
# ... 物理 性 地 直接 呼叫， 您的 指揮部 物理 性 地 將會 瞬間 噴發 數據 ！！
