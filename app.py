import requests
import streamlit as st

def test_jyw_independent_capture(user, pwd, target_url):
    """
    [ 1.08 級別 物理 獨立 測試 鋼印 ]
    物理 性 地 說， 這是 不靠 試算表、 獨立 抓取 的 實彈 測試 ！！
    """
    session = requests.Session()
    # 物理 性的 登入 動作 ( 調用 您 的 鑰匙 )
    login_payload = {"n14184": user, "123": pwd}
    
    try:
        # 1. 物理 性的 登入
        session.post("https://www.moneydj.com/login", data=login_payload)
        # 2. 物理 性的 抓取 ( 找一檔 試算表 沒寫 的 基金 )
        r = session.get(target_url)
        # 3. 物理 性的 邏輯 對位 ( 參考 您 傳給 我的 Apps Script 正則 )
        # ... ( 提取 邏輯 ) ...
        return "物理 獨立 抓取 成功 ！！"
    except:
        return "物理 脫鉤 失敗 ！！"
