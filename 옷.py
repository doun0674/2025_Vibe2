import streamlit as st

st.set_page_config(page_title="이모지 옷 입히기 게임", page_icon="🧸")

st.title("🧸 겹쳐서 입히는 이모지 캐릭터 게임")
st.markdown("얼굴 위에 옷, 모자, 소품을 겹쳐서 캐릭터를 꾸며보세요! 😍")

# 캐릭터 기본 선택
face = st.selectbox("🙂 얼굴 선택", ["🙂", "😎", "😊", "🥳", "😡", "🤖", "👽"])

# 선택 UI
hat = st.selectbox("🧢 모자 선택", ["", "🧢", "🎩", "👑", "🎓", "⛑️", "👒"])
outfit = st.selectbox("👕 옷 선택", ["", "👕", "👗", "🧥", "🎽", "🥋", "🦺"])
accessory = st.selectbox("🎒 소품 선택", ["", "🎒", "🕶️", "🧤", "🧣", "👟", "✨", "⭐"])

# 겹치기 HTML 생성
html = f"""
<div style='position: relative; width: 100px; height: 150px; margin: auto;'>
  <div style='position: absolute; top: -10px; left: 10px; font-size: 50px;'>{hat}</div>
  <div style='position: absolute; top: 40px; left: 10px; font-size: 50px;'>{face}</div>
  <div style='position: absolute; top: 90px; left: 10px; font-size: 50px;'>{outfit}</div>
  <div style='position: absolute; top: 140px; left: 10px; font-size: 40px;'>{accessory}</div>
</div>
"""

# 결과 출력
st.markdown("### 🎨 완성된 캐릭터")
st.markdown(html, unsafe_allow_html=True)

# 리셋
if st.button("🔄 모두 초기화"):
    st.experimental_rerun()

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🎀 이모지를 겹쳐서 입히는 귀여운 캐릭터 꾸미기 🎀</p>", unsafe_allow_html=True)
