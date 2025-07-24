import streamlit as st
import time

st.set_page_config(page_title="2인 클릭 배틀", page_icon="⚔️")

# 초기화
if "p1_score" not in st.session_state:
    st.session_state.p1_score = 0
if "p2_score" not in st.session_state:
    st.session_state.p2_score = 0
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0

GAME_DURATION = 10  # 게임 시간 (초)

st.markdown("<h1 style='text-align:center;'>⚔️ 클릭 배틀: Player 1 vs Player 2</h1>", unsafe_allow_html=True)

# 점수판 표시
score1, score2 = st.columns(2)
score1.metric("👤 Player 1", f"{st.session_state.p1_score} 클릭")
score2.metric("🧑 Player 2", f"{st.session_state.p2_score} 클릭")

st.markdown("---")

# 게임 시작
if not st.session_state.game_started:
    if st.button("🚀 게임 시작!"):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.start_time = time.time()
        st.session_state.game_started = True
        st.experimental_rerun()

# 게임 진행
if st.session_state.game_started:
    elapsed = time.time() - st.session_state.start_time
    time_left = max(0, GAME_DURATION - int(elapsed))

    if time_left > 0:
        st.markdown(f"⏱️ 남은 시간: **{time_left}초**")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("👆 Player 1 클릭!", key="p1_click"):
                st.session_state.p1_score += 1

        with col2:
            if st.button("👆 Player 2 클릭!", key="p2_click"):
                st.session_state.p2_score += 1

        # 실시간 업데이트
        st.experimental_rerun()
    else:
        # 게임 종료
        st.session_state.game_started = False
        st.markdown("---")
        st.subheader("🎉 결과 발표!")

        st.markdown(f"👤 Player 1: **{st.session_state.p1_score}** 클릭")
        st.markdown(f"🧑 Player 2: **{st.session_state.p2_score}** 클릭")

        if st.session_state.p1_score > st.session_state.p2_score:
            st.success("🏆 Player 1 승리!")
        elif st.session_state.p1_score < st.session_state.p2_score:
            st.success("🏆 Player 2 승리!")
        else:
            st.info("🤝 무승부입니다!")

        if st.button("🔁 다시 도전하기"):
            st.session_state.p1_score = 0
            st.session_state.p2_score = 0
            st.session_state.start_time = 0
            st.session_state.game_started = False
            st.experimental_rerun()
