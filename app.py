import streamlit as st

# 物理 性的 「 鑰匙 調用 」 邏輯
def get_jyw_keys():
    try:
        # 物理 性 地 從 Secrets 密室 提取
        user = st.secrets["moneydj"]["n14184"]
        pwd = st.secrets["moneydj"]["123"]
        return user, pwd
    except:
        st.error("物理 密鑰 未 填入 ！！")
        return None, None

# 物理 性的 「 領袖 門禁 」 檢查
def check_master_auth():
    if "authenticated" not in st.session_state:
        # 物理 性 地 彈出 密碼 框
        pwd = st.text_input("請 輸入 領袖 密碼：", type="password")
        if pwd == st.secrets["auth"]["master_password"]:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.stop()
