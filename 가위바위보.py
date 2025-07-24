import streamlit as st
import random

st.set_page_config(page_title="가위바위보 게임", page_icon="🎮")

# 이모지 맵
emoji_map = {
    "가위": "✌",
    "바위": "✊",
    "보": "✋"
}

# 승패 판단 함수
def get_winner(player, computer):
    if player == computer:
        return "무승부 😐"
    elif (player == "가위" and computer == "보") or \
         (player == "바위" and computer == "가위") or \
         (player == "보" and computer == "바위"):
        return "🎉 당신이 이겼어요!"
    else:
        return "😢 컴퓨터가 이겼어요."

# 제목
st.markdown("<h1 style='text-align:center;'>🧸 가위바위보 게임</h1>", unsafe_allow_html=True)
st.markdown("#### 컴퓨터와 귀엽게 한 판 해볼까요?")

# 플레이어 선택
player_choice = st.radio("👇 아래에서 선택하세요!", ["가위", "바위", "보"], horizontal=True)

# 버튼
if st.button("🎮 가위바위보!"):
    # 컴퓨터 선택
    computer_choice = random.choice(["가위", "바위", "보"])
    
    # 승패 판단
    result = get_winner(player_choice, computer_choice)
    
    # 결과 출력
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 👧 당신의 선택")
        st.markdown(f"<div style='font-size:60px;text-align:center'>{emoji_map[player_choice]}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("#### 🤖 컴퓨터의 선택")
        st.markdown(f"<div style='font-size:60px;text-align:center'>{emoji_map[computer_choice]}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f"<h2 style='text-align:center; color: #ff66b2;'>{result}</h2>", unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🎀 귀여운 가위바위보 게임입니다 🎀</p>", unsafe_allow_html=True)
