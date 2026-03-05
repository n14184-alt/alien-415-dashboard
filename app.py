import streamlit as st
import streamlit.components.v1 as components

# PROJECT W - 核心格式校準：黑色字體強化版
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

with st.sidebar:
    st.title("🛡️ 指揮部控制")
    st.write("J.Y.W. 策略：運作中")

html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: "Microsoft JhengHei", sans-serif; background-color: white; }
        table { width: 100%; border-collapse: collapse; }
        th { border-bottom: 2px solid #eee; padding: 12px; text-align: left; color: #444; font-size: 14px; }
        td { border-bottom: 1px solid #eee; padding: 12px; font-size: 15px; color: black; }
        /* 🛡️ 這裡就是你要的：黃底配黑字，保證清晰 */
        .status-box { 
            background-color: #f4b400; 
            color: black; 
            padding: 4px 8px; 
            border-radius: 4px; 
            font-weight: bold; 
            font-size: 13px;
        }
    </style>
</head>
<body>
    <table>
        <tr>
            <th style="width:25%">基金名稱</th>
            <th style="width:12%">當日股價</th>
            <th style="width:12%">效能變動</th>
            <th style="width:5%">率</th>
            <th style="width:18%">監控狀態</th>
            <th style="width:13%">指令對位</th>
            <th style="width:15%">實彈金額</th>
        </tr>
        <tr><td>利安資金韓國</td><td>2.09</td><td>-8.93%</td><td></td><td><span class="status-box">⚠️ 極限進料</span></td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>街口台灣</td><td>121.89</td><td>-6.06%</td><td></td><td><span class="status-box">⚠️ 重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>路博邁台灣 5G 股票</td><td>36.78</td><td>-6.48%</td><td></td><td><span class="status-box">⚠️ 重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>野村 e 科技基金</td><td>150.58</td><td>-6.16%</td><td></td><td><span class="status-box">⚠️ 重度進料</span></td><td>買★★★</td><td>$100,000</td></tr>
        <tr><td>台新台灣中小基金</td><td>184.03</td><td>-5.78%</td><td></td><td><span class="status-box">⚠️ 強力進料</span></td><td>買★★★</td><td>$100,000</td></tr>
    </table>
</body>
</html>
"""
components.html(html_code, height=800, scrolling=True)
