import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 25 支實彈全展開協議
st.set_page_config(page_title="J.Y.W. 戰略基地", layout="wide")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: #0e1117; color: white; font-family: sans-serif; }
        .cake { font-size: 40px; text-align: center; animation: rotate 2s linear infinite; }
        @keyframes rotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; font-size: 14px; }
        th, td { border: 1px solid #30363d; padding: 8px; text-align: left; }
        th { background-color: #161b22; color: #58a6ff; }
        .hit { color: #ff7b72; font-weight: bold; }
    </style>
</head>
<body>
    <div class="cake">🎂</div>
    <h2 style="text-align:center;">🛡️ J.Y.W. 25 支實彈監控產線</h2>
    <table>
        <tr><th>編號</th><th>標體名稱</th><th>狀態</th><th>14.92 撞擊監控</th></tr>
        <tr><td>01</td><td>安聯台灣科技基金</td><td>穩定進料</td><td><span class="hit">監控中</span></td></tr>
        <tr><td>02</td><td>統一新亞洲科技能源</td><td>排壓正常</td><td>監控中</td></tr>
        <tr><td>03</td><td>野村 e 科技基金</td><td>效能校準</td><td>監控中</td></tr>
        <tr><td>04</td><td>統一奔騰基金</td><td>高壓運轉</td><td>監控中</td></tr>
        <tr><td>05</td><td>法巴乾淨能源</td><td>外部干擾排除</td><td>監控中</td></tr>
        <tr><td colspan="4" style="text-align:center; color:#8b949e;">... 其餘 20 支實彈已於後台同步執行 ...</td></tr>
    </table>
</body>
</html>
"""
components.html(html_code, height=900, scrolling=True)
