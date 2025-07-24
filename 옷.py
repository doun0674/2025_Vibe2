import streamlit as st

st.set_page_config(page_title="이모지 옷 입히기", page_icon="🧍")

st.title("🧍 겹쳐 입히는 이모지 캐릭터 게임")
st.markdown("이모지를 겹쳐서 캐릭터를 완성해보세요! 😎")

# 전신 캐릭터 이모지
body = st.selectbox("🙋 캐릭터", ["🧍", "🧍‍♂️", "🧍‍♀️", "🧑‍🎓", "🧑‍🍳", "🧑‍🚀", "🧑‍⚕️"])

# 옵션 선택
hat = st.selectbox("🎩 모자", ["", "🧢", "🎩", "👑", "🎓", "⛑️", "👒"])
outfit = st.selectbox("👕 옷", ["", "👕", "👗", "🧥", "🥋", "🦺", "🎽"])
accessory = st.selectbox("🎒 소품", ["", "🎒", "🧤", "🧣", "👟", "🕶️", "✨", "⭐"])

# 겹쳐서 하나의 레이어로 표현
html = f"""
<div style='position: relative; width: 100px; height: 140px; margin: auto;'>
  <div style='position: absolute; top: 0px; left: 0px; font-size: 64px; z-index: 4;'>{hat}</div>
  <div style='position: absolute; top: 10px; left: 0px; font-size: 64px; z-index: 3;'>{body}</div>
  <div style='position: absolute; top: 10px; left: 0px; font-size: 64px; z-index: 2;'>{outfit}</div>
  <div style='position: absolute; top: 10px; left: 0px; font-size: 64px; z-index: 1;'>{accessory}</div>
</div>
"""

st.markdown("### 🧩 완성된 캐릭터")
st.markdown(html, unsafe_allow_html=True)

if st.button("🔄 리셋"):
    st.experimental_rerun()

st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>✨ 캐릭터를 겹쳐서 꾸며보는 귀여운 이모지 코디 게임 ✨</p>", unsafe_allow_html=True)
