# --- 1.08 級別 曾 氏 通道 物理 顯影 引擎 ( 模擬 版 ) ---
import plotly.graph_objects as go
import numpy as np

def plot_tseng_straight_channel_simulation(df, target_stock):
    try:
        # 物理 性的 「 數據 抓取 」 ( yfinance 模擬 [cite: 2026-03-28] )
        stock_data = df[df['名稱'] == target_stock].iloc[0]
        
        # 模擬 歷史 數據 ( 物理 性 地 這裡 需要 歷史 數據 yfinance )
        # 為了 模擬 出「 直直 的 線 」的 趨勢 [cite: 2026-03-28] ( image_0.png )
        dates = pd.date_range(end=pd.Timestamp.now(), periods=20, freq='D')
        
        # 物理 性的 「 曾 氏 算式 暴力 運算 」 ！！ [cite: 2026-03-28]
        # ( 我們 在 代碼 裡 手動 模擬 出「 直直 的 趨勢 」 [cite: 2026-03-28] )
        # 曾 氏 均線 ( 我們 模擬 了一個 直直 往下 的 均線 趨勢 [cite: 2026-03-28] )
        m, b = np.polyfit(dates.to_julian_date(), df['收盤'].values[:len(dates)], 1) 
        tseng_sma = m * dates.to_julian_date() + b # 物理 性 地 生成 直直 的 線
        
        # 曾 氏 固 定 通道 ( 假設 早上 您 的 曾 氏 標準差 是 固 定 值 0.5% [cite: 2026-03-28] )
        tseng_multiplier = 0.005 
        tseng_upper = tseng_sma * (1 + tseng_multiplier) # 物理 性 地 生成 直直 的 線
        tseng_lower = tseng_sma * (1 - tseng_multiplier) # 物理 性 地 生成 直直 的 線

        # --- 物理 性的 「 圖像 化 渲染 」 ---
        fig = go.Figure()

        # 1. 物理 性 地 繪製 「 股價 彈道 」 ( 模擬 K線 或是 收盤 線 )
        fig.add_trace(go.Scatter(x=dates, y=df['收盤'], name="物理 股價", line=dict(color='#FFD700', width=2)))

        # 2. 物理 性 地 繪製 「 曾 氏 均線 」 [cite: 2026-03-28]
        # 物理 性 地 鎖定 您 要求 的 **「 直直 的 線 」**
        fig.add_trace(go.Scatter(x=dates, y=tseng_sma, name="曾 氏 均線 ( 直 )", line=dict(color='#900c3f', width=1, dash='dash')))

        # 3. 物理 性 地 繪製 「 通道 上 下 軌 」
        # 物理 性 地 鎖定 您 要求 的 **「 直直 的 線 」**
        fig.add_trace(go.Scatter(x=dates, y=tseng_upper, name="曾 氏 上 軌 ( 直 )", line=dict(color='#145a32', width=1)))
        fig.add_trace(go.Scatter(x=dates, y=tseng_lower, name="曾 氏 下 軌 ( 直 )", line=dict(color='#145a32', width=1)))

        # 4. 物理 性的 「 視覺 對位 」 ( 莊家 黑 底 )
        fig.update_layout(
            title=f"🎯 曾 氏 趨勢 物理 顯影 ： {target_stock} ( 模擬 版 )",
            xaxis_title="物理 時間",
            yaxis_title="物理 股價",
            template="plotly_dark",
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
        )
        
        # 物理 性的 「 瞬間 噴發 」 進 Streamlit [cite: 2026-02-18]
        st.plotly_chart(fig, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ 物理 性 顯影 失敗 ！ 原因 ： {e}")
