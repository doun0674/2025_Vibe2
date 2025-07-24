import streamlit as st

st.set_page_config(page_title="👗 이모지 옷 입히기 게임", layout="centered")

st.title("👗 이모지 옷 입히기 게임")
st.markdown("사람 이모지 위에 옷을 겹쳐서 입혀보세요! 👚👖👒")

# 세션 상태 초기화
if "gender" not in st.session_state:
    st.session_state.gender = "🧍"
if "hat" not in st.session_state:
    st.session_state.hat = ""
if "top" not in st.session_state:
    st.session_state.top = ""
if "bottom" not in st.session_state:
    st.session_state.bottom = ""

# 성별 선택
st.subheader("🚻 성별 선택")
gender_choice = st.radio("성별을 선택하세요", ["남성", "여성"], horizontal=True)
if gender_choice == "남성":
    st.session_state.gender = "🧍‍♂️"
else:
    st.session_state.gender = "🧍‍♀️"

# 이모지 옵션
hat_options = {
    "없음": "",
    "🧢 모자": "🧢",
    "🎩 중절모": "🎩",
    "👑 왕관": "👑",
    "⛑️ 헬멧": "⛑️",
    "👒 썬햇": "👒"
}

top_options = {
    "없음": "",
    "👕 티셔츠": "👕",
    "🧥 자켓": "🧥",
    "👚 블라우스": "👚",
    "🥼 실험복": "🥼",
    "👘 기모노": "👘"
}

bottom_options = {
    "없음": "",
    "👖 바지": "👖",
    "👗 원피스": "👗",
    "🩳 반바지": "🩳",
    "👙 비키니": "👙",
    "🩱 수영복": "🩱"
}

# 선택 UI
st.subheader("🧢 모자 선택")
selected_hat = st.radio("모자를 선택하세요", list(hat_options.keys()), horizontal=True)
st.session_state.hat = hat_options[selected_hat]

st.subheader("👕 상의 선택")
selected_top = st.radio("상의를 선택하세요", list(top_options.keys()), horizontal=True)
st.session_state.top = top_options[selected_top]

st.subheader("👖 하의 선택")
selected_bottom = st.radio("하의를 선택하세요", list(bottom_options.keys()), horizontal=True)
st.session_state.bottom = bottom_options[selected_bottom]

# 캐릭터 출력
st.markdown("---")
st.subheader("✨ 당신이 꾸민 캐릭터!")

# CSS를 활용한 이모지 겹치기
character_html = f"""
<div style="display: flex; justify-content: center; align-items: center; position: relative; height: 250px;">
    <div style="font-size: 120px; position: absolute;">{st.session_state.gender}</div>
    <div style="font-size: 120px; position: absolute;">{st.session_state.bottom}</div>
    <div style="font-size: 120px; position: absolute;">{st.session_state.top}</div>
    <div style="font-size: 120px; position: absolute;">{st.session_state.hat}</div>
</div>
"""

st.markdown(character_html, unsafe_allow_html=True)
