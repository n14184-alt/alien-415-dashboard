import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 25 支實彈：適配修復版 (找回左側欄)
st.set_page_config(
    page_title="now 產能監控數據", 
    layout="wide", 
    initial_sidebar_state="expanded" # 🛡️ 強制拉回左邊的東西
)

# 這裡可以放你原本想在左邊看到的雜訊或控制項
with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.write("J.Y.W. 策略監控中")
    st.write("14.92 買進點校準啟動")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { background-color: white; color: black; font-family: "Microsoft JhengHei", sans-serif; }
        table { width: 100%; border-collapse: collapse; font-size: 13px; }
        th { background-color: #f8f9fa; border: 1px solid #ddd; padding: 8px; text-align: left; }
        td { border: 1px solid #eee; padding: 8px; }
        .negative { color: #d93025; font-weight: bold; }
    </style>
</head>
<body>
    <h3 style="color:#202124;">📊 J.Y.W. 25 支實彈：全軍對位監控</h3>
    <table>
        <tr><th>基金名稱</th><th>股價</th><th>效能</th><th>指令</th><th>實彈金額</th></tr>
        <tr><td>利安資金韓國</td><td>2.09</td><td class="negative">-8.93%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>街口台灣</td><td>121.89</td><td class="negative">-6.06%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>路博邁台灣 5G</td><td>36.78</td><td class="negative">-6.48%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>野村 e 科技</td><td>150.58</td><td class="negative">-6.16%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>台新台灣中小</td><td>184.03</td><td class="negative">-5.78%</td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>安聯台灣科技</td><td>443.4</td><td class="negative">-5.48%</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td>統一奔騰</td><td>454.31</td><td class="negative">-5.61%</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td>統一新亞洲</td><td>90.89</td><td class="negative">-5.63%</td><td>買★★</td><td>$50,000</td></tr>
        <tr><td colspan="5" style="text-align:center; color:#70757a;">... 其餘 17 支實彈已全量射入 Slope 監控 ...</td></tr>
    </table>
</body>
</html>
"""
# 縮小高度適配 Win7 螢幕，避免變那麼大
components.html(html_code, height=800, scrolling=True)
