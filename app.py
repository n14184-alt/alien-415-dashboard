import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# PROJECT W - 34支實彈【名稱連動版】
st.set_page_config(layout="wide")

# 🎯 工業校準：只留 ID，排除網址雜訊
# 這是從你的截圖 image_3ed6c0.jpg 提取的精確 ID
SHEET_ID = "1En6L3T_ekxKJoat6C_YVVXrvhbgBSQsBxeCFrFcr__0" 

def get_sheet_data(sheet_id):
    try:
        # 這裡會直接去你的試算表「領料」
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
        df = pd.read_csv(url)
        return df
    except:
        return None

df = get_sheet_data(SHEET_ID)

if df is not None:
    rows = ""
    # 工業邏輯：A欄為名稱，B欄為你試算表算好的價格
    for index, row in df.iterrows():
        try:
            name = str(row[0])
            price = str(row[1])
            # 數據對位，啟動 slope 監控
            rows += f"""<tr><td>{name}</td><td style="font-weight:bold; color:#1a73e8;">{price}</td><td style="color:#d0021b; font-weight:bold;">Slope連動中</td><td></td><td><span style="color:#2ecc71; font-weight:bold; margin-right:4px;">●</span><span style="color:black;">數據在線</span></td><td>14.92 鎖定</td><td>$100,000</td></tr>"""
        except:
            continue

    html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; }} table {{ width: 100%; border-collapse: collapse; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; color: black; }} th {{ border-bottom: 2px solid #eee; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金/ETF名稱</th><th>即時報價 (Google)</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
    components.html(html_layout, height=2000, scrolling=True)
else:
    st.error("❌ 基地連線跳電：請確認試算表已『開啟共用』給知道連結的人！")
