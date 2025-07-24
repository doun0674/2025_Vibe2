import streamlit as st
import random

st.set_page_config(page_title="숫자 맞추기 게임", page_icon="🔢")

st.title("🔢 숫자 맞추기 게임")
st.markdown("### 1부터 100 사이의 숫자를 맞혀보세요!")

# 세션 상태 초기화
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.success = False

# 게임 진행
if not st.session_state.success:
    user_guess = st.number_input("당신의 추측을 입력하세요", min_value=1, max_value=100, step=1)
    if st.button("🎯 정답 확인"):
        st.session_state.tries += 1
        if user_guess < st.session_state.secret_number:
            st.warning("🔼 더 높은 숫자예요!")
        elif user_guess > st.session_state.secret_number:
            st.warning("🔽 더 낮은 숫자예요!")
        else:
            st.success(f"🎉 정답입니다! {st.session_state.tries}번 만에 맞췄어요.")
            st.session_state.success = True
else:
    st.markdown(f"정답은 **{st.session_state.secret_number}**였어요. 잘 하셨어요! 👏")

    if st.button("🔁 다시 시작"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.success = False
        st.experimental_rerun()
