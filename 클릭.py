import streamlit as st

st.set_page_config(page_title="클릭 배틀 게임", page_icon="🖱️")

# 세션 상태 초기화
if "p1_score" not in st.session_state:
    st.session_state.p1_score = 0
if "p2_score" not in st.session_state:
    st.session_state.p2_score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🖱️ 클릭 배틀 게임")
st.markdown("#### 두 사람이 얼마나 빨리 클릭하는지 겨뤄보세요!")

# 게임 진행 중
if not st.session_state.game_over:
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

    st.markdown("---")
    if st.button("🛑 게임 종료"):
        st.session_state.game_over = True

# 게임 종료 후 결과
else:
    st.markdown("### ✅ 게임 종료!")
    st.markdown(f"👤 **Player 1**: {st.session_state.p1_score} 클릭")
    st.markdown(f"🧑 **Player 2**: {st.session_state.p2_score} 클릭")

    if st.session_state.p1_score > st.session_state.p2_score:
        st.success("🎉 Player 1 승리!")
    elif st.session_state.p2_score > st.session_state.p1_score:
        st.success("🎉 Player 2 승리!")
    else:
        st.info("🤝 무승부입니다!")

    if st.button("🔁 다시 시작"):
        st.session_state.p1_score = 0
        st.session_state.p2_score = 0
        st.session_state.game_over = False
        st.experimental_rerun()
