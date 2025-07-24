import streamlit as st

st.set_page_config(page_title="샌드위치 만들기", page_icon="🥪")

st.title("🥪 겹쳐지는 이모지 샌드위치 게임")
st.markdown("재료를 고르고, 겹쳐서 샌드위치를 만들어보세요! 🍅🧀🥓")

# 재료 목록
ingredients = {
    "식빵 🍞": "🍞",
    "치즈 🧀": "🧀",
    "상추 🥬": "🥬",
    "토마토 🍅": "🍅",
    "고기 🍖": "🍖",
    "베이컨 🥓": "🥓",
    "계란후라이 🍳": "🍳",
    "피클 🥒": "🥒",
    "양파 🧅": "🧅",
    "소스 🥫": "🥫",
    "빵뚜껑 🥖": "🥖"
}

# 세션 초기화
if "sandwich_stack" not in st.session_state:
    st.session_state.sandwich_stack = ["🍞"]  # 기본 빵부터 시작

# 재료 추가 버튼
st.markdown("### 🧂 재료 추가")
cols = st.columns(4)
for i, (label, emoji) in enumerate(ingredients.items()):
    if cols[i % 4].button(label):
        st.session_state.sandwich_stack.append(emoji)

# 조작 버튼
st.markdown("### 🔧 조작")
col1, col2 = st.columns(2)
if col1.button("⬅️ 마지막 재료 제거"):
    if len(st.session_state.sandwich_stack) > 1:
        st.session_state.sandwich_stack.pop()
if col2.button("🧹 전체 초기화"):
    st.session_state.sandwich_stack = ["🍞"]

# 겹쳐서 출력
st.markdown("---")
st.markdown("### 🍽️ 완성된 샌드위치 (겹쳐진 단면 보기)")

layers = st.session_state.sandwich_stack

# HTML 생성 (겹쳐진 레이어)
html = "<div style='position: relative; width: 100px; height: 100px; margin: auto;'>"
for i, emoji in enumerate(layers):
    top_offset = 100 - i * 5  # 겹치는 정도
    html += f"<div style='position: absolute; top: {top_offset}px; left: 0px; font-size: 60px; z-index: {i};'>{emoji}</div>"
html += "</div>"

st.markdown(html, unsafe_allow_html=True)

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>✨ 재료를 겹겹이 쌓아 나만의 샌드위치를 완성해보세요! ✨</p>", unsafe_allow_html=True)
