import streamlit as st
import time

st.set_page_config(page_title="클릭 배틀 - 2인 대전", page_icon="⚔️")

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

st.title("⚔️ 2인 클릭 대결 게임")
st.markdown("#### 제한 시간 10초 동안 누가 더 많이 클릭하는지 겨뤄보세요!")

# 게임 시작
if not st.session_state.game_started:
    if st.button("🚀 게임 시작!"):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.start_time = time.time()
        st.session_state.game_started = True
        st.experimental_rerun()

# 게임 진행 중
if st.session_state.game_started:
    elapsed = time.time() - st.session_state.start_time
    time_left = max(0, GAME_DURATION - int(elapsed))

    if time_left > 0:
        st.markdown(f"⏱️ 남은 시간: **{time_left}초**")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("👤 Player 1")
            if st.button("👆 클릭!", key="p1"):
                st.session_state.p1_score += 1
            st.markdown(f"**클릭 수:** {st.session_state.p1_score}")

        with col2:
            st.subheader("🧑 Player 2")
            if st.button("👆 클릭!", key="p2"):
                st.session_state.p2_score += 1
            st.markdown(f"**클릭 수:** {st.session_state.p2_score}")

        st.experimental_rerun()  # 실시간 갱신

    else:
        # 게임 종료
        st.session_state.game_started = False
        st.markdown("---")
        st.subheader("🎉 결과 발표!")

        st.markdown(f"👤 Player 1: **{st.session_state.p1_score} 클릭**")
        st.markdown(f"🧑 Player 2: **{st.session_state.p2_score} 클릭**")

        if st.session_state.p1_score > st.session_state.p2_score:
            st.success("🏆 Player 1 승리!")
        elif st.session_state.p1_score < st.session_state.p2_score:
            st.success("🏆 Player 2 승리!")
        else:
            st.info("🤝 무승부입니다!")

        if st.button("🔄 다시 시작"):
            st.session_state.game_started = False
            st.session_state.p1_score = 0
            st.session_state.p2_score = 0
            st.experimental_rerun()
