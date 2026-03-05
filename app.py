import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 180°C 高壓全自動產線
st.set_page_config(page_title="now 產能監控數據", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: white; color: black; font-family: "Microsoft JhengHei", sans-serif; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; border: 1px solid #ddd; }
        th { background-color: #f8f9fa; border-bottom: 2px solid #eee; padding: 12px; text-align: left; color: #5f6368; }
        td { border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; }
        .negative { color: #d93025; font-weight: bold; } /* 負效能變動顯示紅色 */
        .buy-stars { color: #202124; font-weight: bold; }
        .warning-icon { color: #fbbc04; margin-right: 5px; }
    </style>
</head>
<body>
    <h3 style="color:#202124;">📊 now 產能監控數據 (25 支實彈全方位對位)</h3>
    <table>
        <tr><th>基金名稱</th><th>當日股價</th><th>效能變動</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>
        <tr><td>利安資金韓國</td><td>2.09</td><td class="negative">-8.93%</td><td>⚠️極限進料</td><td class="buy-stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>街口台灣</td><td>121.89</td><td class="negative">-6.06%</td><td>⚠️重度進料</td><td class="buy-stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>路博邁台灣 5G 股票</td><td>36.78</td><td class="negative">-6.48%</td><td>⚠️重度進料</td><td class="buy-stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>野村 e 科技基金</td><td>150.58</td><td class="negative">-6.16%</td><td>⚠️重度進料</td><td class="buy-stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>台新台灣中小基金</td><td>184.03</td><td class="negative">-5.78%</td><td>⚠️強力進料</td><td class="buy-stars">買★★★</td><td>$100,000</td></tr>
        <tr><td>安聯台灣科技基金</td><td>443.4</td><td class="negative">-5.48%</td><td>⚠️強力進料</td><td class="buy-stars">買★★</td><td>$50,000</td></tr>
        <tr><td>統一奔騰基金</td><td>454.31</td><td class="negative">-5.61%</td><td>⚠️強力進料</td><td class="buy-stars">買★★</td><td>$50,000</td></tr>
        <tr><td>統一新亞洲科技能源</td><td>90.89</td><td class="negative">-5.63%</td><td>⚠️強力進料</td><td class="buy-stars">買★★</td><td>$50,000</td></tr>
        <tr><td>摩根大通關鍵科技</td><td>...</td><td>...</td><td>監控中</td><td>待對位</td><td>$50,000</td></tr>
        <tr><td colspan="6" style="text-align:center; color:#70757a;">... 其餘實彈標的已同步於後台執行 Slope 校準 ...</td></tr>
    </table>
</body>
</html>
"""
components.html(html_code, height=1200, scrolling=True)
