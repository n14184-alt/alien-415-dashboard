import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup
import time

# PROJECT W - 25支實彈強力抓取引擎 (抗干擾強化版)
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

def JYW_GET_NAV(url):
    try:
        # 強力投料：模擬真實瀏覽器行為，排除外部干擾
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Referer': 'https://www.moneydj.com/'
        }
        r = requests.get(url, headers=headers, timeout=10)
        r.encoding = 'utf-8' # 校準編碼
        soup = BeautifulSoup(r.text, 'html.parser')
        # 精準定位淨值數據 (MoneyDJ 專屬工業對位)
        nav_element = soup.find("div", {"class": "t3n2"})
        if nav_element:
            return nav_element.text.strip()
        return "定位失效"
    except Exception as e:
        return f"排壓中:{str(e)[:5]}"

# 🏗️ 25 支精銳實彈：全量自動化
fund_data = [
    {"name": "安聯台灣科技基金", "id": "ACDD04"}, {"name": "統一新亞洲科技能源", "id": "UPT02B"},
    {"name": "野村 e 科技基金", "id": "ACKL01"}, {"name": "台新台灣中小基金", "id": "ACTS03"},
    {"name": "統一奔騰基金", "id": "ACPS10-PS03"}, {"name": "利安資金韓國基金", "id": "LIC04"},
    {"name": "街口台灣單一國家", "id": "ACPS10-PS03"}, {"name": "路博邁台灣 5G 股票", "id": "ACNB11"},
    {"name": "摩根日本(日圓)基金", "id": "JFZ13"}, {"name": "復華大中華中小策略", "id": "ACFH30"},
    {"name": "統一黑馬基金", "id": "ACPS04"}, {"name": "安聯台灣大壩基金", "id": "ACDD01"},
    {"name": "野村中小基金", "id": "ACKL03"}, {"name": "群益奧爾科技基金", "id": "ACCC11"},
    {"name": "摩根台灣金磚基金", "id": "ACJF09"}, {"name": "匯豐台灣精選基金", "id": "ACHB01"},
    {"name": "日盛小而美基金", "id": "ACJS04"}, {"name": "富邦長江基金", "id": "ACFB18"},
    {"name": "國泰中小成長基金", "id": "ACIT03"}, {"name": "保德信高成長基金", "id": "ACDT01"},
    {"name": "元大卓越基金", "id": "ACYT01"}, {"name": "兆豐國際第一基金", "id": "ACKI01"},
    {"name": "第一金電子基金", "id": "ACFS01"}, {"name": "華南永昌物聯網", "id": "ACSW09"},
    {"name": "凱基雲端趨勢基金", "id": "ACKG10"}
]

rows = ""
for f in fund_data:
    url = f"https://www.moneydj.com/funddj/ya/yp010000.djhtm?a={f['id']}"
    nav = JYW_GET_NAV(url)
    rows += f"""<tr><td>{f['name']}</td><td style="font-weight:bold; color:black;">{nav}</td><td style="color:#d0021b; font-weight:bold;">Slope連動中</td><td></td><td><span style="color:#f4b400; font-weight:bold; margin-right:4px;">⚠️</span><span style="color:black; font-weight:bold;">監控中</span></td><td>14.92 鎖定</td><td>$100,000</td></tr>"""

html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; background-color: white; color: black; }} table {{ width: 100%; border-collapse: collapse; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; color: black; white-space: nowrap; }} th {{ border-bottom: 2px solid #eee; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金名稱</th><th>當日淨值</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
components.html(html_layout, height=1800, scrolling=True)
