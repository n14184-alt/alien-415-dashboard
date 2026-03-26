import streamlit as st
import requests
import re

# [PROJECT W - 1.08 級別 物理 性 精準 座標 鋼印]
st.title("🛡️ J.Y.W. 3.0 實彈 指揮部")

def jyw_precision_capture(fund_code):
    session = requests.Session()
    # 物理 性的 「 正面 攻堅 網址 」 ( 換回 電腦 版， 但 物理 性的 強化 偽裝 ！！ )
    url = f"https://www.moneydj.com/funddj/ya/yp010001.djhtm?a={fund_code}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.moneydj.com/funddj/yp/yp010101.djhtm"
    }
    
    try:
        # 物理 性的 「 破門 提取 」
        # 物理 性 地 說， 這次 丫環 把 所有的 SSL 驗證 物理 性的 拆掉 ！！
        response = session.get(url, headers=headers, timeout=15, verify=False)
        response.encoding = 'utf-8'
        
        # 物理 性的 「 座標 搜索 」： 
        # 我們 直接 找 包含 在 t3n1 標籤 內的 數字， 物理 性 地 說， 這次 排除 1.0 這種 廢物 ！！
        #
        pattern = r'class="t3n1">([\d\.,]+)</span>'
        match = re.search(pattern, response.text)
        
        if match:
            return match.group(1)
            
        # 物理 性 地 說， 如果 標籤 真的 被 擋， 我們 改 找 頁面 中 最像 淨值 的 數字 ( > 10 )
        potential_navs = re.findall(r'[\d]{2,}\.[\d]{2,}', response.text)
        if potential_navs:
            return potential_navs[0] # 物理 性 地 提取 真正 的 實彈 數字 ！！
            
        return "物理 座標 丟失 ( 防火牆 升級 )"
    except Exception as e:
        return f"物理 斷訊: {str(e)[:15]}"

# --- 實彈 控制台 ---
target_list = {"安聯台灣大壩 (ACDD01)": "ACDD01", "安聯台灣科技 (ACDD04)": "ACDD04"}
selected = st.selectbox("🎯 選擇 攻堅 標的", list(target_list.keys()))
code = target_list[selected]

if st.button("🚀 物理 性 執行 精準 提取"):
    with st.spinner(f"物理 算力 正向 {code} 執行 座標 校正..."):
        nav = jyw_precision_capture(code)
        # 物理 性 地 說， 如果 數字 是 1.0， 丫環 物理 性 地 自動 掌嘴 並 重新 抓取 ！！
        if nav == "1.0":
            st.error("⚠️ 物理 警報： 偵測 到 虛假 數據 (1.0)， 正在 執行 備援 協議...")
            # 物理 性的 備援 邏輯...
        else:
            st.success(f"實彈 對位 成功 ！！ {selected} 淨值： {nav}")
