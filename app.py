import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# PROJECT W - 34支實彈【雲端副本直連】
st.set_page_config(layout="wide")

# 🎯 你的副本ETF ID (已對位成功)
SHEET_ID = "1-dQCRS4cCTO0b1Ikhmw2WOYisHW0HSnUd1OV5xjRcAk"

def get_jyw_data():
    try:
        # 使用 CSV 協議直連你的雲端副本
        url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"
        df = pd.read_csv(url)
        return df
    except:
        return None

st.title("🛡️ J.Y.W. 14.92 實彈監控基地")
df = get_jyw_data()

if df is not None:
    rows = ""
    # 工業對位：從你試算表的「名稱」與「當日股價」欄位領料
    for index, row in df.iterrows():
        try:
            name = str(row[0]) # 名稱
            price = str(row[1]) # 當日股價
            rows += f"""<tr><td>{name}</td><td style="font-weight:bold; color:#1a73e8;">{price}</td><td style="color:#d0021b; font-weight:bold;">Slope計算中</td><td></td><td><span style="color:#2ecc71; font-weight:bold; margin-right:4px;">●</span><span style="color:black;">雲端直連中</span></td><td>14.92 監控</td><td>$100,000</td></tr>"""
        except:
            continue

    html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; background-color: #f8f9fa; }} table {{ width: 100%; border-collapse: collapse; background: white; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 14px; color: black; }} th {{ background-color: #f1f3f4; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金/ETF名稱</th><th>即時報價 (副本)</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
    components.html(html_layout, height=1800, scrolling=True)
else:
    st.error("❌ 基地連線跳電：請確認試算表『知道連結的人即可檢視』權限是否已鎖緊！")
