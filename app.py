import requests
import pandas as pd

def fetch_official_data_demo():
    """
    [ 1.08 級別 物理 性 官方 API 鋼印 ]
    物理 性 地 直接 呼叫 證交所 或 政府 開放 平台 API
    """
    # 物理 性的 範例： 抓取 上市 個股 行情 ( Open Data 接口 )
    url = "https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_AVG_ALL"
    
    try:
        # 物理 性 地 直接 向 官方 伺服器 拿 數據
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            # 物理 性 地 說， 這 就是 您的 「 官方 實彈 數據 」 ！！
            return df
        return "官方 接口 暫時 關閉"
    except Exception as e:
        return f"物理 異常: {str(e)[:15]}"

# --- 物理 性 的 戰略 接續 ---
# 老闆， 物理 性 地 說， 安聯 與 統一 這種 「 基金 」 淨值， 
# 官方 的 OpenAPI 通常 更新 較 慢 ( 隔日 )。
