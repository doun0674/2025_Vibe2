import streamlit as st

st.set_page_config(page_title="이모지 옷 입히기 게임", page_icon="👗")

st.title("🧸 이모지 옷 입히기 게임")
st.markdown("### 이모지로 내 캐릭터를 꾸며보세요! 😍")

# 기본 캐릭터 얼굴
CHARACTER_FACE = st.selectbox("🙂 얼굴 선택", ["🙂", "😎", "😊", "🥳", "😡", "🤖", "👽"])

# 선택된 아이템 저장
if "selected_items" not in st.session_state:
    st.session_state.selected_items = []

# 카테고리별 이모지
emoji_categories = {
    "👕 옷": ["👕", "👗", "🧥", "🩳", "🩱", "🎽", "🥋", "🦺"],
    "🧢 모자": ["🧢", "🎩", "👑", "🎓", "⛑️", "👒"],
    "🎒 소품": ["🕶️", "🎒", "👟", "👞", "🧤", "🧣", "🧦"],
    "🎭 재미 요소": ["🐱‍🏍", "🦸‍♀️", "🦹‍♂️", "👻", "🎃", "🦄"],
    "🧙‍♂️ 마법/특수효과": ["🪄", "🪐", "⭐", "💫", "✨", "🌀"]
}

# UI - 이모지 카테고리별 선택
st.markdown("### 🎨 이모지를 선택해서 꾸며보세요!")
for category, emojis in emoji_categories.items():
    with st.expander(category):
        cols = st.columns(len(emojis))
        for i, emoji in enumerate(emojis):
            if cols[i].checkbox(emoji, key=f"{category}_{emoji}"):
                if emoji not in st.session_state.selected_items:
                    st.session_state.selected_items.append(emoji)
            else:
                if emoji in st.session_state.selected_items:
                    st.session_state.selected_items.remove(emoji)

# 캐릭터 출력
st.markdown("---")
st.markdown("### ✨ 완성된 캐릭터 ✨")
outfit_line = " ".join(st.session_state.selected_items)
st.markdown(f"<h1 style='text-align:center'>{CHARACTER_FACE}<br>{outfit_line}</h1>", unsafe_allow_html=True)

# 초기화
if st.button("🔄 모두 벗기기 / 리셋"):
    st.session_state.selected_items = []

# 푸터
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>🎀 다양한 이모지로 나만의 스타일을 표현해보세요 🎀</p>", unsafe_allow_html=True)
