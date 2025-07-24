import streamlit as st

st.set_page_config(page_title="샌드위치 만들기 게임", page_icon="🥪")

st.title("🥪 이모지 샌드위치 만들기 게임")
st.markdown("재료를 골라서 이모지로 샌드위치를 쌓아보세요!")

# 세션 상태 초기화
if "sandwich_stack" not in st.session_state:
    st.session_state.sandwich_stack = ["🍞"]  # 시작은 식빵

# 재료 목록
ingredients = {
    "식빵 🍞": "🍞",
    "치즈 🧀": "🧀",
    "상추 🥬": "🥬",
    "토마토 🍅": "🍅",
    "고기 🍖": "🍖",
    "베이컨 🥓": "🥓",
    "계란 🍳": "🍳",
    "피클 🥒": "🥒",
    "양파 🧅": "🧅",
    "소스 🥫": "🥫",
    "빵뚜껑 🥖": "🥖"
}

# UI - 재료 선택
st.markdown("### 🧂 재료 선택")
cols = st.columns(4)
for i, (label, emoji) in enumerate(ingredients.items()):
    if cols[i % 4].button(label):
        st.session_state.sandwich_stack.insert(0, emoji)  # 위에 쌓기

# UI - 재료 제거
st.markdown("### 🔧 조작")
col1, col2 = st.columns(2)
if col1.button("⬆️ 위 재료 제거"):
    if len(st.session_state.sandwich_stack) > 1:
        st.session_state.sandwich_stack.pop(0)
if col2.button("🧹 전체 초기화"):
    st.session_state.sandwich_stack = ["🍞"]

# 샌드위치 시각화
st.markdown("---")
st.markdown("### 🍽️ 나만의 샌드위치")
sandwich_html = "<div style='text-align:center; font-size:60px; line-height: 1;'>"
for layer in st.session_state.sandwich_stack[::-1]:  # 아래부터 위로 쌓기
    sandwich_html += f"{layer}<br>"
sandwich_html += "</div>"

st.markdown(sandwich_html, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🧡 나만의 이모지 샌드위치를 만들고 친구와 공유해보세요!</p>", unsafe_allow_html=True)

