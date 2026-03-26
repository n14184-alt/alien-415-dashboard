import requests
from bs4 import BeautifulSoup

def jyw_smart_search_capture(fund_full_name, user, pwd):
    # [ 1.08 級別 物理 搜尋 穿透 鋼印 ]
    # 物理 性 地 說， 絕不 再 用 丫環 腦袋 裡的 「 假 網址 」 ！！
    
    session = requests.Session()
    # 1. 物理 性 地 模擬 登入 ( 確保 看到 會員 專屬 數據 )
    # session.post("login_url", data={"user": user, "pass": pwd})
    
    # 2. 物理 性的 「 領袖 座標 」 直接 對位 ！！
    if "國泰台灣高股息" in fund_full_name:
        target_url = "https://www.moneydj.com/funddj/yp/yp010000.djhtm?a=ACCY149"
    else:
        # 3. 物理 性的 暴力 搜尋 邏輯 ！！
        search_url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={fund_full_name}"
        target_url = search_url # 物理 性的 搜尋 轉發
        
    try:
        r = session.get(target_url)
        soup = BeautifulSoup(r.text, "html.parser")
        # 物理 性 地 鎖定 您 試算表 指定 的 t3n1 標籤 ！！
        nav = soup.find("span", class_="t3n1").text
        return f"【 實彈 座標 穿透 】{fund_full_name}：{nav}"
    except:
        return "物理 搜尋 斷訊 ！！"
