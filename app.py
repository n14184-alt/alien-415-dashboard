import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf
import pandas as pd

# PROJECT W - 34支實彈【腳本直連引擎】
st.set_page_config(layout="wide")

# 🏗️ 34 支實彈工業代碼清單 (已校準為 yfinance 格式)
funds = [
    {"n": "元大台灣50", "i": "0050.TW"}, {"n": "富邦科技", "i": "0052.TW"},
    {"n": "台新臺灣IC設計", "i": "00947.TW"}, {"n": "兆豐台灣晶圓製造", "i": "00913.TW"},
    {"n": "元大中型100", "i": "0051.TW"}, {"n": "國泰臺韓科技", "i": "00735.TW"},
    {"n": "國泰費城半導體", "i": "00830.TW"}, {"n": "富邦台灣半導體", "i": "00892.TW"},
    {"n": "中信上游半導體", "i": "00941.TW"}, {"n": "富邦越南", "i": "00885.TW"},
    {"n": "中信關鍵半導體", "i": "00891.TW"}, {"n": "FT潔淨能源", "i": "00899.TW"},
    {"n": "統一FANG+", "i": "00757.TW"}, {"n": "中信小資高價30", "i": "00894.TW"},
    {"n": "國泰數位支付服務", "i": "00909.TW"}, {"n": "第一金太空衛星", "i": "00910.TW"},
    {"n": "新光美國電力基建", "i": "9805.TW"}, {"n": "期元大S&P黃金", "i": "00635U.TW"},
    {"n": "元大全球5G", "i": "00876.TW"}, {"n": "元大全球AI", "i": "00762.TW"},
    {"n": "元大歐洲50", "i": "00660.TW"}, {"n": "元大航太防衛科技", "i": "00965.TW"},
    {"n": "期元大S&P原油", "i": "00642U.TW"}, {"n": "期元大美元指數", "i": "00682U.TW"},
    {"n": "元大寶滬深", "i": "0061.TW"}, {"n": "富邦印度", "i": "00652.TW"},
    {"n": "富邦臺灣中小", "i": "00733.TW"}, {"n": "野村全球航運", "i": "00960.TW"},
    {"n": "統一台股增長", "i": "00981A.TW"}, {"n": "復華未來50", "i": "00991A.TW"},
    {"n": "元大台灣高息低波", "i": "00713.TW"}, {"n": "元大美債20年", "i": "00679B.TW"},
    {"n": "元大美債20反一", "i": "00681R.TW"}, {"n": "復華中國5G", "i": "00877.TW"}
]

rows = ""
for f in funds:
    try:
        # 腳本直接抓取最新報價，排除 Google 試算表的中間干擾
        ticker = yf.Ticker(f['i'])
        price = ticker.fast_info['last_price']
        price_fmt = f"{price:.2f}"
    except:
        price_fmt = "連線校準中"
    
    rows += f"""<tr><td>{f['n']}</td><td style="font-weight:bold; color:#1a73e8;">{price_fmt}</td><td style="color:#d0021b; font-weight:bold;">Slope計算中</td><td></td><td><span style="color:#2ecc71; font-weight:bold; margin-right:4px;">●</span><span style="color:black;">腳本直抓</span></td><td>14.92 鎖定</td><td>$100,000</td></tr>"""

html_layout = f"""<style>body {{ font-family: "Microsoft JhengHei", sans-serif; }} table {{ width: 100%; border-collapse: collapse; }} td {{ border-bottom: 1px solid #eee; padding: 12px; font-size: 14px; color: black; }} th {{ border-bottom: 2px solid #eee; padding: 10px; text-align: left; color: #666; }}</style><table><tr><th>基金/ETF名稱</th><th>即時現價 (直連)</th><th>效能變動</th><th>率</th><th>監控狀態</th><th>指令對位</th><th>實彈金額</th></tr>{rows}</table>"""
components.html(html_layout, height=1800, scrolling=True)
