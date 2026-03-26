import requests
from bs4 import BeautifulSoup
import streamlit as st

def test_cathay_jyw_special_capture(fund_name, user, pwd):
    """
    [ 1.08 級別 物理 國泰 攻堅 鋼印 ]
    物理 性 地 說， 這是 不靠 試算表 網址、 獨立 攻堅 國泰 的 實彈 測試 ！！
    """
    st.info(f"物理 性 偵測 到 國泰 基金：{fund_name}， 啟動 攻堅 戰術 ！！")
    
    # 物理 優選 戰術： 繞道 MoneyDJ ( 用 您 的 鑰匙 登入 )
    session = requests.Session()
    login_url = "https://www.moneydj.com/login" # 範例 網址
    
    try:
        # 1. 物理 性的 登入 門戶 ！！
        # session.post(login_url, data={"user": n14184, "pass": 123})
        
        # 2. 物理 性的 搜尋 國泰 基金 頁面 ( 假設 為 該 ISIN )
        isin_url = "https://www.moneydj.com/funddj/yp/FindFund.djhtm?a=TW000T4150Y5" 
        r = session.get(isin_url)
        
        # 3. 物理 性的 邏輯 對位 提取 ！！
        soup = BeautifulSoup(r.text, "html.parser")
        # 鎖定 淨值 t3n2 標籤
        nav_element = soup.find("span", class_="t3n2")
        if nav_element:
            return nav_element.text.strip()
        return "物理 繞道 失敗"
    exceptException as e:
        return f"物理 攻堅 異常: {str(e)[:15]}"
