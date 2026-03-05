import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# PROJECT W - 34支實彈【試算表同步版】
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# 🏗️ 指揮官，請把你的試算表網址中那串長長的 ID 貼在下面引號內
# 例如: https://docs.google.com/spreadsheets/d/這串就是ID/edit
SHEET_ID = ""https://docs.google.com/spreadsheets/d/1En6L3T_ekxKJoat6C_YVVXRvhbgBSQsBxeCFrFcr__0/edit?usp=sharing"" 

def get_sheet_data(sheet_id):
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
        df = pd.read_csv(url)
        return df
    except:
        return None

# 📡 執行效能校準與數據輸出
df = get_sheet_data(SHEET_ID)

if df is not None:
    rows = ""
    for index, row in df.iterrows():
        # 這裡會自動對應你的 A 欄(名稱)與 B 欄(價格)
        name = row[0]
        price = row[1]
        rows += f"""<tr><td>{name}</td><td style="font-weight:bold;">{price}</td><td style="color:#d0021b; font-weight:bold;">Slope計算中</td><td></td><td><span style="color:#f4b400; font-weight:bold; margin-right:4px;">⚠️</span><span style="color:black; font-weight:bold;">監控中</span></td><td>14.92 鎖定</td><td>$100,000</td></tr>"""

    html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; background-color: white; color: black; }} table {{ width: 100%; border-collapse: collapse; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; color: black; white-space: nowrap; }} th {{ border-bottom: 2px solid #eee; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金/ETF名稱</th><th>當日現價</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
    components.html(html_layout, height=1800, scrolling=True)
else:
    st.error("❌ 基地對位失敗：請確認試算表已開啟「知道連結的人即可檢視」權限。")
