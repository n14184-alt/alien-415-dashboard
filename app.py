def fetch_fund_nav_by_isin(isin_code):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") # 物理 性 避開 雲端 權限 封鎖
    chrome_options.add_argument("--disable-dev-shm-usage") # 物理 性 避免 記憶體 崩潰
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # [ 1.08 級別 物理 性 修正 ]： 強制 指定 雲端 瀏覽器 路徑
    chrome_options.binary_location = "/usr/bin/chromium" 
    
    # 物理 性 地 啟動， 不再 依賴 自動 下載， 直接 呼叫 您的 packages.txt 零件
    from selenium.webdriver.chrome.service import Service
    service = Service("/usr/bin/chromedriver")
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        search_url = f"https://www.moneydj.com/funddj/yp/FindFund.djhtm?a={isin_code}"
        driver.get(search_url)
        
        # 物理 性 執行 您 傳授 的 「 擬人 戰術 」
        time.sleep(2)
        driver.back()
        time.sleep(1)
        driver.forward()
        
        wait = WebDriverWait(driver, 20)
        nav_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "t3n2")))
        nav_value = nav_element.text
        return nav_value
    except Exception as e:
        return f"物理 錯誤: {str(e)[:30]}"
    finally:
        driver.quit()
