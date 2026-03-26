import yfinance as yf

def fetch_fund_nav_by_isin_v2(isin):
    """
    [方案二]： 物理 性 yfinance 數據 映射 ！！ ( 走 API 通道 )
    """
    # 物理 性的 映射 碼 ( 假設 安聯 在 Yahoo 的 代號 為此 )
    # 注意： 某些 基金 在 Yahoo 可能 需 使用 特定 Ticker
    ticker_map = {
        "TW000T3604Y3": "0050.TW", # 此為 示例， 需 根據 實際 Ticker 調整
        "TW000T0910ACY7": "0056.TW"
    }
    
    try:
        ticker = ticker_map.get(isin)
        if ticker:
            data = yf.Ticker(ticker)
            price = data.history(period="1d")['Close'].iloc[-1]
            return f"{price:.2f}"
        return "方案二 無 映射 碼"
    except:
        return "方案二 抓取 失敗"
