import streamlit as st
import random

st.set_page_config(page_title="🎯 숫자 맞추기 게임", page_icon="🔢")

st.markdown("<h1 style='text-align:center;'>🎯🔢 숫자 맞추기 게임 🔢🎯</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>🧠 1부터 100 사이의 숫자를 맞춰보세요! 🎁</p>", unsafe_allow_html=True)
st.markdown(" ")

# 세션 상태 초기화
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.success = False
    st.session_state.history = []

# 게임 중
if not st.session_state.success:
    user_guess = st.number_input("📝 숫자를 입력하세요!", min_value=1, max_value=100, step=1, format="%d")
    
    if st.button("🎯 정답 확인하기! 🔍"):
        st.session_state.tries += 1
        st.session_state.history.append(user_guess)

        if user_guess < st.session_state.secret_number:
            st.warning("🔼 더 높은 숫자예요! 📈")
            st.balloons()
        elif user_guess > st.session_state.secret_number:
            st.warning("🔽 더 낮은 숫자예요! 📉")
            st.snow()
        else:
            st.success(f"🎉 정답입니다! 🎉 {st.session_state.tries}번 만에 맞췄어요! 🏆🥳")
            st.balloons()
            st.session_state.success = True

        # 추측 히스토리 보여주기
        st.markdown("📜 **지금까지의 추측들:**")
        st.markdown(" 👉 " + " | ".join([f"{n}🔍" for n in st.session_state.history]))

# 정답 맞춘 후
else:
    st.markdown("🌈 **게임 클리어!** 🌈")
    st.markdown(f"✅ 정답은 **{st.session_state.secret_number}**이었어요! 대단해요! 👏👏")
    st.markdown(f"🔁 시도 횟수: {st.session_state.tries}번 ⏱️")

    if st.button("🔄 다시 시작하기 🎮"):
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.success = False
        st.session_state.history = []
        st.experimental_rerun()

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🎲 재미있는 숫자 게임! 친구와 함께 즐겨보세요 🎲</p>", unsafe_allow_html=True)
