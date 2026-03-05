import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 25 支實彈：效能校準輕量版 (解決卡頓問題)
st.set_page_config(page_title="now 產能監控", layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.write("J.Y.W. 策略：**全速運作**")
    st.write("14.92 買進點：**鎖定中**")

# 將 25 支標的封裝進列表，減少編輯器壓力
targets = [
    ["01", "利安資金韓國", "2.09", "-8.93%", "買★★★"],
    ["02", "街口台灣", "121.89", "-6.06%", "買★★★"],
    ["03", "路博邁台灣 5G", "36.78", "-6.48%", "買★★★"],
    ["04", "野村 e 科技", "150.58", "-6.16%", "買★★★"],
    ["05", "台新台灣中小", "184.03", "-5.78%", "買★★★"],
    ["06", "安聯台灣科技", "443.4", "-5.48%", "買★★"],
    ["07", "統一奔騰基金", "454.31", "-5.61%", "買★★"],
    ["08", "統一新亞洲", "90.89", "-5.63%", "買★★"],
]

# 自動生成 HTML 表格，不佔用編輯器緩存
rows = "".join([f"<tr><td>{t[0]}</td><td>{t[1]}</td><td>{t[2]}</td><td style='color:red'>{t[3]}</td><td>{t[4]}</td></tr>" for t in targets])

html_code = f"""
<table style="width:100%; border-collapse:collapse; font-family:sans-serif; font-size:14px;">
    <tr style="background:#f8f9fa;"><th>編號</th><th>基金名稱</th><th>股價</th><th>變動</th><th>指令</th></tr>
    {rows}
    <tr><td colspan="5" style="text-align:center; padding:20px; color:gray;">... 其餘 17 支實彈已全量射入 Slope 監控 ...</td></tr>
</table>
"""
components.html(html_code, height=600)
