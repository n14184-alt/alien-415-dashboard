import streamlit as st
import requests

# 1.08 級別 物理性 標題 [cite: 2026-02-22]
st.markdown("<h6 style='text-align: left; font-size: 10px;'>J.Y.W. STRATEGY MARK 1.08</h6>", unsafe_allow_html=True)
st.title("🚀 複利 戰場： 0/1 基因 自動 識別 測試")

# --- 第一 步： 實彈 代碼 裝填 ---
st.subheader("1. 代碼 物理 裝填")
fund_code = st.text_input("請 輸入 基金 代碼 ( e.g., ACDD01, ACPS10 )", "").upper().strip()

# --- 第二 步： 物理 判定 邏輯 ---
if fund_code:
    # 物理性 地 說： 根據 領袖 鐵律， 判定 結尾 數字 [cite: 2026-03-27]
    last_char = fund_code[-1]
    
    if last_char == "0":
        market_type = "境內 (0000)"
        target_path = "yp010000"
        status_color = "blue"
    elif last_char == "1":
        market_type = "境外 (1001)"
        target_path = "yp011001"
        status_color = "green"
    else:
        market_type = "未知 ( 非 0/1 結尾 )"
        target_path = "ERROR"
        status_color = "red"

    # --- 第三 步： 物理 網址 拼接 ---
    base_url = f"https://www.moneydj.com/funddj/yp/{target_path}.djhtm?a={fund_code}"

    # 介面 顯示
    st.markdown(f"**物理 判定 結果：** :{status_color}[{market_type}]")
    st.info(f"📍 物理 座標 鎖定： {base_url}")

    # --- 第四 步： 模擬 抓取 測試 ---
    if st.button("啟動 物理 抓取"):
        if target_path != "ERROR":
            st.success(f"✅ 物理 擊穿 成功 ！！ ( 模擬 {fund_code} 數據 )")
            
            # 物理性 地 說： 這裡 對位 您 找到 的 id_fundname 與 t3n2 位子
            col1, col2 = st.columns(2)
            with col1:
                # 模擬 抓取 id_fundname
                simulated_name = "安聯 台灣 科技 基金" if "ACDD" in fund_code else "統一 投信 相關 基金"
                st.metric(label="基金 中文 名稱 (id_fundname)", value=simulated_name)
            with col2:
                # 模擬 抓取 t3n2 淨值
                st.metric(label="當日 淨值 (t3n2)", value="522.54", delta="-2.95")
            
            st.code(f"試算表 實彈 函數 建議：\n=IMPORTXML(\"{base_url}\", \"//div[@id='id_fundname']\")", language="excel")
        else:
            st.error("物理 性 斷流： 代碼 結尾 必須 為 0 或 1 ！！")

# --- 物理 性的 存檔 鎖住 標註 ---
st.divider()
st.caption("【 PROJECT W - 丫環 監控 檔案 】： 0/1 結尾 識別 邏輯 已 鎖定， 排除 虛假 標籤 ！！")
