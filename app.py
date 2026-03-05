import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components

# PROJECT W - 14.92 實彈爬蟲版
st.set_page_config(layout="wide")

def get_twse_price():
    try:
        # 直接對位證交所 MI_INDEX 進料口
        url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=json&type=ALL'
        res = requests.get(url)
        data = res.json()
        # 提取收盤行情 (第9組數據)
        df = pd.DataFrame(data['data9'], columns=data['fields9'])
        return df
    except:
        return None

# 🏗️ 34 支實彈代號 (對應 image_3e806b.png)
target_ids = ["0050", "0052", "00947", "00913", "0051", "00735", "00830", "00892", "00941", "00885", "00891", "00899", "00757", "00894", "00909", "00910", "9805", "00635U", "00876", "00762", "00660", "00965", "00642U", "00682U", "0061", "00652", "00733", "00960", "00981A", "00991A", "00713", "00679B", "00681R", "00877"]

df_all = get_twse_price()

rows = ""
if df_all is not None:
    # 執行工業過濾：只留老闆的戰略標的
    df_jyw = df_all[df_all['證券代號'].isin(target_ids)]
    for _, item in df_jyw.iterrows():
        rows += f"""<tr><td>{item['證券名稱']}</td><td style="font-weight:bold; color:#1a73e8;">{item['收盤價']}</td><td style="color:#d0021b; font-weight:bold;">Slope同步中</td><td></td><td><span style="color:#2ecc71; font-weight:bold; margin-right:4px;">●</span><span style="color:black;">證交所直連</span></td><td>14.92 鎖定</td><td>$100,000</td></tr>"""

html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; }} table {{ width: 100%; border-collapse: collapse; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 14px; color: black; }} th {{ border-bottom: 2px solid #eee; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金/ETF名稱</th><th>當日收盤 (實時)</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
components.html(html_layout, height=1800, scrolling=True)
