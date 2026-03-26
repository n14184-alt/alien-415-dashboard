import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# [PROJECT W - 1.08 級別 數據 鋼印 存檔 鎖住] 
# 物理 性 地 執行 領袖 之 ISIN 唯一 辨識 戰略 [cite: 2026-03-24]

def fetch_fund_nav(isin_code):
    """
    物理 性 地 模擬 人類 行為， 透過 ISIN 碼 穿透 MoneyDJ 密室 抓取 淨值
    """
    # 1. 物理 性的 擬人 化 配置
    chrome_options = Options()
    chrome_options.add_argument("--headless") # 物理 性 地 隱身 抓取
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # 2. 物理 性的 鑰匙 對位： 直接 進入 MoneyDJ 基金 淨值 搜尋 頁面
        # 物理 性 地 說， 這裡 透過 搜尋 接口 模擬 您 的 鑰匙 插入
        search_url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin_code}"
        driver.get(search_url)
        
        # 3. 執行 領袖 傳授 之 「 回 上 一 頁 再 回來 」 戰術
        # 物理 性 地 閃避 防 爬 偵測， 重置 網頁 狀態
        time.sleep(random.uniform(1.2, 2.5))
        driver.back()
        time.sleep(random.uniform(0.8, 1.5))
        driver.forward()
        
        # 4. 物理 性的 密室 提取： 等待 淨值 數字 出現
        wait = WebDriverWait(driver, 15)
        # 物理 性 地 定位 淨值 欄位 ( 此 為 MoneyDJ 常用 標籤 結構 )
        nav_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "t3n2")))
        
        nav_value = nav_element.text
        fund_name = driver.title.split('-')[0].strip()
        
        print(f"【 物理 成功 】 標的：{fund_name} | ISIN: {isin_code} | 最 新 淨值: {nav_value}")
        return nav_value

    except Exception as e:
        print(f"【 物理 警報 】 ISIN {isin_code} 抓取 失敗： 密室 鎖定 中 ...")
        return None
    finally:
        driver.quit()

# --- 1.08 級別 實彈 測試 區 ---
if __name__ == "__main__":
    # 老題 物理 性 指定 之 2 支 傳奇 基金
    test_targets = [
        "TW000T3604Y3", # 安聯 台灣 科技 基金
        "TW000T0910ACY7" # 統一 奔騰 基金
    ]
    
    print(f"--- 啟動 J.Y.W. 3.0： 物理 性 封神 測試 --- [cite: 2026-03-24]")
    for isin in test_targets:
        fetch_fund_nav(isin)
        # 物理 性的 呼吸 延遲， 確保 0 屏蔽
        time.sleep(random.uniform(3, 5))
