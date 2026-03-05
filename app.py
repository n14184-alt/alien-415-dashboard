import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 核心格式修復檔案 (180°C 純淨進料)
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.write("J.Y.W. 策略：**監控中**")
    st.write("14.92 點位：**全天候鎖定**")

# 🏗️ 恢復 8:04 黑字純淨格式：三角型單獨黃、文字純黑
html_code = """
<style>
    body { font-family: "Microsoft JhengHei", sans-serif; background-color: white; color: black; }
    table { width: 100%; border-collapse: collapse; }
    th { border-bottom: 2px solid #eee; padding: 10px; text-align: left; font-size: 14px; color: #666; white-space: nowrap; }
    td { border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; white-space: nowrap; color: black; }
    .warning-icon { color: #f4b400; font-weight: bold; margin-right: 4px; font-size: 16px; }
    .status-text { color: black; font-weight: bold; }
    .neg { color: #d0021b; font-weight: bold; }
</style>
<table>
    <tr><th>基金名稱</th><th>當日股價</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>
    <tr><td>利安資金韓國基金</td><td>2.09</td><td class="neg">-8.93%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">極限進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>街口台灣單一國家</td><td>121.89</td><td class="neg">-6.06%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>路博邁台灣 5G 股票</td><td>36.78</td><td class="neg">-6.48%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>野村 e 科技基金</td><td>150.58</td><td class="neg">-6.16%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>台新台灣中小基金</td><td>184.03</td><td class="neg">-5.78%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    <tr><td>安聯台灣科技基金</td><td>443.4</td><td class="neg">-5.48%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★</td><td>$50,000</td></tr>
    <tr><td>統一奔騰基金</td><td>454.31</td><td class="neg">-5.61%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★</td><td>$50,000</td></tr>
    <tr><td>統一新亞洲科技能源</td><td>90.89</td><td class="neg">-5.63%</td><td></td><td><span class="warning-icon">⚠️</span><span class="status-text">強力進料</span></td><td>買★★</td><td>$50,000</td></tr>
    <tr><td colspan="7" style="text-align:center; color:gray; padding:20px;">... 其餘實彈 Slope 監控中 ...</td></tr>
</table>
"""
components.html(html_code, height=900, scrolling=True)
