import streamlit as st

st.set_page_config(page_title="겹쳐 입히기 실험", page_icon="👗")

st.title("👗 겹쳐 입히기 이모지 캐릭터")

# 사용자 선택
face = st.selectbox("🙂 얼굴 선택", ["🙂", "😎", "😊", "😡"])
outfit = st.selectbox("🧥 옷 선택", ["", "👕", "👗", "🧥"])
hat = st.selectbox("🎩 모자 선택", ["", "🧢", "👑", "🎓"])

# HTML로 겹쳐 표현
html_code = f"""
<div style='position: relative; width: 120px; height: 150px; margin: auto;'>
  <div style='position: absolute; top: 0px; left: 0px; font-size: 64px;'>{hat}</div>
  <div style='position: absolute; top: 30px; left: 0px; font-size: 64px;'>{face}</div>
  <div style='position: absolute; top: 75px; left: 0px; font-size: 64px;'>{outfit}</div>
</div>
"""

st.markdown(html_code, unsafe_allow_html=True)
