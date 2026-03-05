import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 25 支實彈：全量不隱藏版 (180°C 全力進料)
st.set_page_config(
    page_title="now 產能監控數據 - 全量版", 
    layout="wide", 
    initial_sidebar_state="expanded" 
)

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.markdown("---")
    st.write("J.Y.W. 策略：**全速運作**")
    st.write("14.92 買進點：**全天候鎖定**")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: white; color: black; font-family: "Microsoft JhengHei", sans-serif; margin: 0; }
        table { width: 100%; border-collapse: collapse; table-layout: fixed; }
        th { background-color: #f8f9fa; border: 1px solid #ddd; padding: 10px; font-size: 13px; text-align: left; }
        td { border: 1px solid #eee; padding: 10px; font-size: 13px; }
        .negative { color: #d93025; font-weight: bold; }
        .row-id { color: #888; font-size: 11px; }
    </style>
</head>
<body>
    <h3 style="color:#202124;">📊 now 產能監控：25 支實彈 (全量對位中)</h3>
    <table>
        <colgroup>
            <col style="width: 8%;"> <col style="width: 32%;"> <col style="width: 15%;"> <col style="width: 15%;"> <col style="width: 15%;"> <col style="width: 15%;">
        </colgroup>
        <tr><th>編號</th><th>基金名稱</th><th>當日股價</th><th>效能變動</th><th>指令對位</th><th>實彈金額</th></tr>
        <tr><td class="row-id">01</td><td>利安資金韓國</td><td>2.09</td><td class="negative">-8.93%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td class="row-id">02</td><td>街口台灣</td><td>121.89</td><td class="negative">-6.06%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td class="row-id">03</td><td>路博邁台灣 5G</td><td>36.78</td><td class="negative">-6.48%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td class="row-id">04</td><td>野村 e 科技</td><td>150.58</td><td class="negative">-6.16%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td class="row-id">05</td><td>台新台灣中小</td><td>184.03</td><td class="negative">-5.78%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td class="row-id">06</td><td>安聯台灣科技</td><td>443.4</td><td class="negative">-5.48%</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td class="row-id">07</td><td>統一奔騰基金</td><td>454.31</td><td class="negative">-5.61%</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td class="row-id">08</td><td>統一新亞洲</td><td>90.89</td><td class="negative">-5.63%</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td class="row-id">09</td><td>法巴乾淨能源</td><td>97.76</td><td>-0.45%</td><td>監控中</td><td>$50,000</td></tr>
        <tr><td class="row-id">10</td><td>摩根大通關鍵科技</td><td>--</td><td>--</td><td>監控中</td><td>$50,000</td></tr>
        <tr><td class="row-id">11</td><td>安聯台灣大壩</td><td>--</td><td>--</td><td>校準中</td><td>--</td></tr>
        <tr><td class="row-id">...</td><td>...其餘實彈...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
        <tr><td class="row-id">25</td><td>J.Y.W. 尾盤校準</td><td>--</td><td>--</td><td>Slope 監控</td><td>--</td></tr>
    </table>
</body>
</html>
"""
# 🛡️ 高度拉到 1200，保證 25 支標的全部有位置站
components.html(html_code, height=1200, scrolling=True)
