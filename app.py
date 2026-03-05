import streamlit as st
import streamlit.components.v1 as components
import requests
import pandas as pd
from io import StringIO
from datetime import datetime

# PROJECT W - 34支實彈【證交所直投版】
st.set_page_config(layout="wide")

def JYW_GET_STOCK_PRICE():
    try:
        # 自動抓取最近一個交易日的數據 (工業進料校準)
        datestr = datetime.now().strftime('%Y%m%d')
        url = f'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date={datestr}&type=ALL'
        r = requests.get(url)
        
        # 排除雜訊與排壓：整理 CSV
        raw_data = r.text.split("\n")
        data = [l for l in raw_data if len(l.split('",')) >= 10 and l[0] != '=']
        df = pd.read_csv(StringIO("\n".join(data)))
        
        # 清理逗號雜訊
        df = df.apply(lambda s: s.astype(str).str.replace(",", "").str.replace('"', ''))
        return df
    except:
        return None

# 🏗️ 34 支實彈 ID 清單 (排除雜訊，只留代號)
target_ids = ["0050", "0052", "00947", "00913", "0051", "00735", "00830", "00892", "00941", "00885", "00891", "00899", "00757", "00894", "00909", "00910", "9805", "00635U", "00876", "00762", "00660", "00965", "00642U", "00682U", "0061", "00652", "00733", "00960", "00981A", "00991A", "00713", "00679B", "00681R", "00877"]

df_all = JYW_GET_STOCK_PRICE()

rows = ""
if df_all is not None:
    # 只篩選出老闆要的 34 支實彈
    df_jyw = df_all[df_all['證券代號'].isin(target_ids)]
    for _, item in df_jyw.iterrows():
        rows += f"""<tr><td>{item['證券名稱']} ({item['證券代號']})</td><td style="font-weight:bold; color:#1a73e8;">{item['收盤價']}</td><td style="color:#d0021b; font-weight:bold;">Slope連動</td><td></td><td><span style="color:#2ecc71; font-weight:bold; margin-right:4px;">●</span><span style="color:black;">證交所直通</span></td><td>14.92 鎖定</td><td>$100,000</td></tr>"""

html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; }} table {{ width: 100%; border-collapse: collapse; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 14px; color: black; }} th {{ border-bottom: 2px solid #eee; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金/ETF名稱</th><th>即時現價 (證交所)</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
components.html(html_layout, height=1800, scrolling=True)
