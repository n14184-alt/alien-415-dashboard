import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 25 支實彈：終極解析度適配 (解決字體疊字)
st.set_page_config(
    page_title="now 產能監控數據", 
    layout="wide", 
    initial_sidebar_state="expanded" 
)

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.markdown("---")
    st.write("J.Y.W. 策略：**監控中**")
    st.write("14.92 買進點：**已鎖定**")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: white; color: black; font-family: "Microsoft JhengHei", sans-serif; margin: 0; }
        table { width: 100%; border-collapse: collapse; table-layout: fixed; } /* 🛡️ 強制固定比例防止疊字 */
        th { background-color: #f8f9fa; border: 1px solid #ddd; padding: 6px; font-size: 12px; color: #5f6368; }
        td { border: 1px solid #eee; padding: 6px; font-size: 12px; white-space: nowrap; overflow: hidden; }
        .negative { color: #d93025; font-weight: bold; }
        .stars { font-weight: bold; color: #202124; }
    </style>
</head>
<body>
    <h4 style="margin-bottom:10px;">📊 產能對位：25 支實彈全監控</h4>
    <table>
        <colgroup>
            <col style="width: 35%;"> <col style="width: 15%;"> <col style="width: 15%;"> <col style="width: 15%;"> <col style="width: 20%;">
        </colgroup>
        <tr><th>基金名稱</th><th>當日股價</th><th>效能變動</th><th>指令對位</th><th>實彈金額</th></tr>
        <tr><td>利安資金韓國</td><td>2.09</td><td class="negative">-8.93%</td><td class="stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>街口台灣</td><td>121.89</td><td class="negative">-6.06%</td><td class="stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>路博邁台灣 5G</td><td>36.78</td><td class="negative">-6.48%</td><td class="stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>野村 e 科技</td><td>150.58</td><td class="negative">-6.16%</td><td class="stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>台新台灣中小</td><td>184.03</td><td class="negative">-5.78%</td><td class="stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>安聯台灣科技</td><td>443.4</td><td class="negative">-5.48%</td><td class="stars">買★★</td><td>$50,000</td></tr>
        <tr><td>統一奔騰基金</td><td>454.31</td><td class="negative">-5.61%</td><td class="stars">買★★</td><td>$50,000</td></tr>
        <tr><td>統一新亞洲</td><td>90.89</td><td class="negative">-5.63%</td><td class="stars">買★★</td><td>$50,000</td></tr>
    </table>
    <p style="font-size:10px; color:gray; margin-top:10px;">... 其餘 17 支實彈已射入後台 Slope 監控中 ...</p>
</body>
</html>
"""
components.html(html_code, height=600, scrolling=True)
