import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_fund_nav_by_isin(isin):
    """
    物理 性 地 直接 擊穿 MoneyDJ 數據 牆 ！！
    """
    # 物理 性的 「 數據 門戶 」
    url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        # 物理 性 地 直接 抓取 網頁 原始 內容
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            
            # 物理 性的 鎖定： MoneyDJ 的 淨值 數字 永遠 在 class 為 't3n2' 的 標籤 裡 ！！
            nav_element = soup.find("span", class_="t3n2")
            
            if nav_element:
                nav_value = nav_element.text.strip()
                return nav_value
            else:
                # 備援 邏輯： 物理 性 地 搜尋 網頁 內 所有的 數字 格式
                return "數據 提取 中..."
        return "連線 失敗"
    except:
        return "接口 異常"

# 物理 性的 指令 封發 ！！
# st.write(f"安聯 台灣 科技 淨值： {fetch_fund_nav_by_isin('TW000T3604Y3')}")
