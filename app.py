import streamlit as st
import requests

# J.Y.W. 3.0 基金 實彈 介面
st.title("J.Y.W. 3.0 Fund Tracker")

# 物理 性 鎖定 ID: 136KQ4C1o9XwxOTzN1D7Zdvrls4tIW0Fi6Eq8JuiQMlk
fund_input = st.text_input("Enter Fund Code (e.g., ACDD01):", "")

if fund_input:
    # 物理 性 提示: 這裡 必須 填入 您 發佈 後 的 GAS Web App URL
    gas_url = "https://script.google.com/macros/s/您的ID/exec" 
    
    try:
        response = requests.get(f"{gas_url}?code={fund_input}")
        data = response.json()
        
        if data.get('price') and data['price'] != 0:
            st.success(f"Fund: {fund_input} | Price: {data['price']}")
        else:
            st.error("Data Not Found (Check Spreadsheet A column)")
            
    except Exception as e:
        st.warning(f"Connection Error: {e}")
