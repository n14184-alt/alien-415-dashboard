import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import random

# [PROJECT W - 1.08 級別 雲端 環境 物理 修正]
# 物理 性 地 解決 Streamlit Cloud 之 Chromium 路徑 鎖定 問題

def fetch_fund_nav_by_isin(isin_code):
    chrome_options = Options()
    
    # 物理 性的 「 雲端 隱身 參數 」 疊加
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    # 物理 性的 「 絕對 路徑 」 鋼印 ( 針對 您的 packages.txt 零件 )
    # 物理 性 地 說， Streamlit Cloud 的 chromium 物理 座標 在此
    chrome_options.binary_location = "/usr/bin/chromium"
    
    try:
        # 物理 性 地 手動 指定 Service， 徹底 關閉 自動 偵測
        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 物理 性 地 插入 ISIN 鑰匙
        search_url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin_code}"
        driver.get(search_url)
        
        # 執行 領袖 傳授 之 「 擬人 刷新 術 」
        time.sleep(2)
        driver.back()
        time.sleep(1)
        driver.forward()
        
        # 提取 數據 ... ( 略， 同 前面 邏輯 )
        nav_element = driver.find_element("class name", "t3n2")
        nav_value = nav_element.text
        return nav_value
        
    except Exception as e:
        # 物理 性 地 捕捉 錯誤 並 顯示 在 儀表板， 方便 領袖 監控
        st.error(f"物理 抓取 失敗: {str(e)}")
        return "抓取 失敗"
    finally:
        if 'driver' in locals():
            driver.quit()
