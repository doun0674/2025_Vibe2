import streamlit as st
import random

st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🎯")

st.markdown("<h1 style='text-align:center;'>🎯 숫자 맞추기 게임</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>1부터 100 사이의 숫자를 맞혀보세요!</p>", unsafe_allow_html=True)

# 세션 상태 초기화
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.history = []

# 숫자 입력
user_guess = st.number_input("🔢 숫자를 입력하세요!", min_value=1, max_value=100, step=1)

# 정답 확인
if st.button("🎯 정답 확인하기"):
    st.session_state.tries += 1
    st.session_state.history.append(user_guess)

    if user_guess < st.session_state.secret_number:
        st.warning("🔼 더 높은 숫자예요!")
    elif user_guess > st.session_state.secret_number:
        st.warning("🔽 더 낮은 숫자예요!")
    else:
        st.success(f"🎉 정답입니다! {st.session_state.tries}번 만에 맞췄어요!")
        st.balloons()
        # 자동 초기화
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.history = []
        st.info("🔄 새로운 숫자가 설정되었습니다! 다시 도전해보세요! 🎮")

# 히스토리 출력
if st.session_state.history:
    st.markdown("📜 지금까지의 추측:")
    st.markdown(" 👉 " + " | ".join([f"{n}🔍" for n in st.session_state.history]))

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🎲 재미있는 숫자 게임! 계속 도전해보세요 🎲</p>", unsafe_allow_html=True)
