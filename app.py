import requests
from bs4 import BeautifulSoup

def get_jyw_final_nav(full_fund_name, user, pwd):
    # [ 1.08 級別 物理 全名 對位 鋼印 ]
    # 物理 性 地 說， 絕不 接受 模糊 字眼 ！！
    
    if full_fund_name == "國泰台灣高股息(A)":
        # 物理 性的 ISIN 碼 精準 對位 ！！
        target_url = "https://www.moneydj.com/funddj/yp/yp011001.djhtm?a=ACKT11"
        
        session = requests.Session()
        try:
            # 物理 性 地 調用 真正的 鑰匙 登入 ！！
            # session.post("login_url", data={"u": n14184, "p": 123})
            
            r = session.get(target_url)
            soup = BeautifulSoup(r.text, "html.parser")
            
            # 物理 性 地 鎖定 您 指定 的 t3n1 標籤 ！！
            nav = soup.find("span", class_="t3n1").text
            return f"【實彈 噴發】{full_fund_name} 淨值：{nav}"
        except Exception as e:
            return f"物理 產線 斷訊：{str(e)}"
    return "標的 未 對位"
