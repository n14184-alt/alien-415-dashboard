import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 核心格式校準 (依照老闆 7:53 指令)
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.write("J.Y.W. 策略運作中")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; }
        table { width: 100%; border-collapse: collapse; table-layout: fixed; }
        th { border-bottom: 2px solid #eee; padding: 12px; text-align: left; color: #555; font-size: 14px; }
        td { border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; }
        .warning { color: #f4b400; font-weight: bold; } /* ⚠️ 監控狀態標誌 */
        .negative { font-weight: bold; }
    </style>
</head>
<body>
    <table>
        <tr>
            <th style="width:25%">基金名稱</th>
            <th style="width:15%">當日股價</th>
            <th style="width:15%">效能變動</th>
            <th style="width:5%">率</th>
            <th style="width:15%">監控狀態</th>
            <th style="width:10%">指令對位</th>
            <th style="width:15%">實彈金額</th>
        </tr>
        <tr><td>利安資金韓國</td><td>2.09</td><td class="negative">-8.93%</td><td></td><td class="warning">⚠️ 極限進料</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>街口台灣</td><td>121.89</td><td class="negative">-6.06%</td><td></td><td class="warning">⚠️ 重度進料</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>路博邁台灣 5G 股票</td><td>36.78</td><td class="negative">-6.48%</td><td></td><td class="warning">⚠️ 重度進料</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>野村 e 科技基金</td><td>150.58</td><td class="negative">-6.16%</td><td></td><td class="warning">⚠️ 重度進料</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>台新台灣中小基金</td><td>184.03</td><td class="negative">-5.78%</td><td></td><td class="warning">⚠️ 強力進料</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>安聯台灣科技基金</td><td>443.4</td><td class="negative">-5.48%</td><td></td><td class="warning">⚠️ 強力進料</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td>統一奔騰基金</td><td>454.31</td><td class="negative">-5.61%</td><td></td><td class="warning">⚠️ 強力進料</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td>統一新亞洲科技能源</td><td>90.89</td><td class="negative">-5.63%</td><td></td><td class="warning">⚠️ 強力進料</td><td>買★★</td><td>$50,000</td></tr>
    </table>
</body>
</html>
"""
components.html(html_code, height=800, scrolling=True)
