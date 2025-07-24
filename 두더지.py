import streamlit as st
import random
import time

st.set_page_config(page_title="두더지 잡기 게임", page_icon="🦫")

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "mole_index" not in st.session_state:
    st.session_state.mole_index = random.randint(0, 8)
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "start_time" not in st.session_state:
    st.session_state.start_time = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

GAME_TIME = 20  # 게임 제한 시간 (초)
GRID_SIZE = 3   # 3x3 그리드

st.title("🦫 두더지 잡기 게임")
st.markdown("#### 제한 시간 20초 동안 주더지를 최대한 많이 잡아보세요!")

# 게임 시작
if not st.session_state.game_started:
    if st.button("🚀 게임 시작!"):
        st.session_st_
