import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# [PROJECT W - 1.08 級別 數據 鋼印 存檔 鎖住] 
# 物理 性 地 執行 領袖 之 「 ISIN 唯一 驅動 」 核心 戰略 [cite: 2026-03-24]

def fetch_fund_nav_by_isin(isin_code):
    """
    物理 性 地 透過 ISIN 鑰匙 穿透 MoneyDJ 密室， 執行 領袖 指定 之 2 支 基金 實測
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless") # 物理 性的 隱身 抓取
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # 1. 物理 性的 鑰匙 插入： MoneyDJ 搜尋 接口
        search_url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin_code}"
        driver.get(search_url)
        
        # 2. 物理 性的 「 擬人 刷新 」
        # 物理 性 地 執行 領袖 傳授 之 「 回 上 一 頁 再 回來 」 戰術， 確保 0 屏蔽
        time.sleep(random.uniform(1.5, 2.5))
        driver.back()
        time.sleep(random.uniform(1.0, 1.8))
        driver.forward()
        
        # 3. 物理 性的 密室 提取： 定位 淨值 標籤
        wait = WebDriverWait(driver, 15)
        # 物理 性 地 鎖定 淨值 欄位 ( MoneyDJ 經典 結構 )
        nav_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "t3n2")))
        
        nav_value = nav_element.text
        # 物理 性 地 抓取 標的 名稱 ( 從 網頁 標題 提取 )
        fund_name = driver.title.split('-')[0].strip()
        
        print(f"【 物理 成功 】 標的：{fund_name} | ISIN: {isin_code} | 最 新 淨值: {nav_value}")
        return nav_value

    except Exception as e:
        print(f"【 物理 警報 】 ISIN {isin_code} 抓取 失敗： 鑰匙 可能 已 被 網站 物理 隔離 ！！")
        return None
    finally:
        driver.quit()

# --- 1.08 級別 雙 標的 實彈 演習 ---
if __name__ == "__main__":
    # 老闆 物理 性 欽點 之 兩 把 鑰匙
    isin_keys = [
        "TW000T3604Y3", # 安聯 台灣 科技 基金
        "TW000T0910ACY7" # 統一 奔騰 基金
    ]
    
    print(f"--- 啟動 J.Y.W. 3.0： ISIN 核心 實彈 抓取 --- [cite: 2026-03-24]")
    for key in isin_keys:
        fetch_fund_nav_by_isin(key)
        # 物理 性的 呼吸 間隔， 確保 0 屏蔽 鋼印
        time.sleep(random.uniform(4, 6))
