import streamlit as st

st.set_page_config(page_title="👗 이모지 옷 입히기 게임", layout="centered")

st.title("👗 이모지 옷 입히기 게임")
st.markdown("이모지들이 겹쳐서 실제로 옷 입힌 것처럼 보이게 만들었어요! 👚👖👒")

# 세션 상태 초기화
if "gender" not in st.session_state:
    st.session_state.gender = "🧍‍♂️"
if "hat" not in st.session_state:
    st.session_state.hat = ""
if "top" not in st.session_state:
    st.session_state.top = ""
if "bottom" not in st.session_state:
    st.session_state.bottom = ""

# 성별 선택
st.subheader("🚻 성별 선택")
gender_choice = st.radio("성별을 선택하세요", ["남성", "여성"], horizontal=True)
st.session_state.gender = "🧍‍♂️" if gender_choice == "남성" else "🧍‍♀️"

# 이모지 옵션
hat_options = {
    "없음": "",
    "🧢": "🧢",
    "🎩": "🎩",
    "👑": "👑",
    "⛑️": "⛑️",
    "👒": "👒"
}

top_options = {
    "없음": "",
    "👕": "👕",
    "🧥": "🧥",
    "👚": "👚",
    "🥼": "🥼",
    "👘": "👘"
}

bottom_options = {
    "없음": "",
    "👖": "👖",
    "👗": "👗",
    "🩳": "🩳",
    "👙": "👙",
    "🩱": "🩱"
}

# 선택 UI
st.subheader("🧢 모자")
selected_hat = st.radio("모자를 골라주세요", list(hat_options.keys()), horizontal=True)
st.session_state.hat = hat_options[selected_hat]

st.subheader("👕 상의")
selected_top = st.radio("상의 이모지를 골라주세요", list(top_options.keys()), horizontal=True)
st.session_state.top = top_options[selected_top]

st.subheader("👖 하의")
selected_bottom = st.radio("하의 이모지를 골라주세요", list(bottom_options.keys()), horizontal=True)
st.session_state.bottom = bottom_options[selected_bottom]

# 출력
st.markdown("---")
st.subheader("✨ 옷을 입힌 캐릭터")

character_html = f"""
<div style="position: relative; height: 430px; width: 250px; margin: auto;">
    <!-- 사람 -->
    <div style="position: absolute; top: 100px; left: 0px; font-size: 200px; z-index: 1;">{st.session_state.gender}</div>

    <!-- 하의 (다리 쪽) -->
    <div style="position: absolute; top: 170px; left: 0px; font-size: 200px; z-index: 2;">{st.session_state.bottom}</div>

    <!-- 상의 (몸통) -->
    <div style="position: absolute; top: 90px; left: 0px; font-size: 200px; z-index: 3;">{st.session_state.top}</div>

    <!-- 모자 (머리 위) -->
    <div style="position: absolute; top: 20px; left: 0px; font-size: 200px; z-index: 4;">{st.session_state.hat}</div>
</div>
"""

st.markdown(character_html, unsafe_allow_html=True)
