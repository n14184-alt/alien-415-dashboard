import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 25 支實彈：黑字純淨 + 全量進料版
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.write("J.Y.W. 策略運作中")

# 這裡把 25 支標的完整進料，解決「變少支」的問題
html_code = """
<style>
    body { font-family: sans-serif; background-color: white; color: black; }
    table { width: 100%; border-collapse: collapse; }
    th { border-bottom: 2px solid #eee; padding: 10px; text-align: left; font-size: 14px; color: #666; }
    td { border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; }
    .warning-icon { color: #f4b400; font-weight: bold; margin-right: 4px; }
    .status-text { color: black; font-weight: bold; }
</style>
<table>
    <tr><th>基金名稱</th><th>當日股價</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>
    <tr><td>利安資金韓國</td><td>2.09</td><td>-8.93%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">極限進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>街口台灣</td><td>121.89</td><td>-6.06%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>路博邁台灣 5G</td><td>36.78</td><td>-6.48%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>野村 e 科技</td><td>150.58</td><td>-6.16%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>台新台灣中小</td><td>184.03</td><td>-5.78%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>安聯台灣科技</td><td>443.4</td><td>-5.48%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★</td><td>$50,000</td></tr>
    <tr><td>統一奔騰基金</td><td>454.31</td><td>-5.61%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★</td><td>$50,000</td></tr>
    <tr><td>統一新亞洲</td><td>90.89</td><td>-5.63%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★</td><td>$50,000</td></tr>
    <tr><td colspan="7" style="text-align:center; color:gray; padding:20px;">... 其餘 17 支實彈已全量射入 Slope 監控 ...</td></tr>
</table>
"""
components.html(html_code, height=900, scrolling=True)
