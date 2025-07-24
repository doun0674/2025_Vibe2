import streamlit as st

# 16가지 MBTI 유형 상세 정보
mbti_details = {
    "ISTJ": {
        "title": "🧱 ISTJ - 현실주의자형",
        "desc": "책임감 있고 현실적인 성향의 소유자로, 전통과 질서를 중요시하고 계획에 따라 행동합니다.",
        "strengths": "신뢰성, 체계적 사고, 책임감",
        "weaknesses": "융통성 부족, 감정 표현 어려움",
        "jobs": "회계사, 행정직, 군인, 판사",
        "famous": "나폴레옹, 조지 워싱턴"
    },
    "ISFJ": {
        "title": "🛡️ ISFJ - 수호자형",
        "desc": "온화하고 책임감 있는 성격으로, 다른 사람을 배려하고 돕는 데 큰 만족을 느낍니다.",
        "strengths": "성실함, 헌신적, 세심한 관찰력",
        "weaknesses": "자기 주장 부족, 변화에 대한 저항",
        "jobs": "간호사, 사회복지사, 교사",
        "famous": "비욘세, 케이트 미들턴"
    },
    "INFJ": {
        "title": "🌌 INFJ - 옹호자형",
        "desc": "깊은 통찰력과 이상을 가진 사람으로, 세상을 더 나은 방향으로 이끌고자 합니다.",
        "strengths": "이해심, 창의성, 직관력",
        "weaknesses": "과도한 이상 추구, 내면 감정 억제",
        "jobs": "상담가, 작가, 인권 운동가",
        "famous": "마틴 루터 킹 주니어, 넬슨 만델라"
    },
    "INTJ": {
        "title": "🔮 INTJ - 전략가형",
        "desc": "독립적이고 분석적인 사고를 바탕으로 장기적인 목표를 계획하고 달성하는 데 강점이 있습니다.",
        "strengths": "논리적, 독창적, 자기주도적",
        "weaknesses": "완벽주의, 감정에 둔감함",
        "jobs": "전략기획자, 과학자, 프로그래머",
        "famous": "일론 머스크, 스티븐 호킹"
    },
    "INFP": {
        "title": "🌷 INFP - 중재자형",
        "desc": "이상주의적이며 자기 신념과 가치를 중시하는 사람으로, 타인의 감정을 깊이 공감합니다.",
        "strengths": "공감 능력, 창의성, 도덕적 신념",
        "weaknesses": "현실 회피, 비판에 민감함",
        "jobs": "작가, 심리상담가, 예술가",
        "famous": "윌리엄 셰익스피어, 조니 뎁"
    },
    "ENTP": {
        "title": "⚡ ENTP - 발명가형",
        "desc": "호기심 많고 재치 있는 성격으로, 새로운 아이디어나 도전을 추구합니다.",
        "strengths": "창의성, 말솜씨, 유연한 사고",
        "weaknesses": "지속성 부족, 규칙 무시",
        "jobs": "기획자, 창업가, 변호사",
        "famous": "로버트 다우니 주니어, 마크 트웨인"
    },
    "ENFP": {
        "title": "🌈 ENFP - 활동가형",
        "desc": "열정적이고 사교적인 성격으로, 새로운 사람과의 관계를 통해 에너지를 얻습니다.",
        "strengths": "낙천적, 열정적, 감정 표현 능력",
        "weaknesses": "주의 산만, 감정 기복",
        "jobs": "마케터, 배우, 교사",
        "famous": "로빈 윌리엄스, 샤를리즈 테론"
    },
    "ESFJ": {
        "title": "🤝 ESFJ - 집정관형",
        "desc": "타인의 감정에 민감하고 조화를 중요시하는 따뜻한 리더입니다.",
        "strengths": "친절함, 협동성, 사교성",
        "weaknesses": "과도한 걱정, 타인의 시선 의식",
        "jobs": "교사, 간호사, 커뮤니티 매니저",
        "famous": "테일러 스위프트, 휴 그랜트"
    },
    "ENTJ": {
        "title": "👑 ENTJ - 통솔자형",
        "desc": "천성적인 리더로 전략과 효율을 중요시하며 강한 추진력을 가지고 있습니다.",
        "strengths": "결단력, 리더십, 체계적 사고",
        "weaknesses": "권위적, 감정 무시",
        "jobs": "CEO, 변호사, 관리자",
        "famous": "스티브 잡스, 고든 램지"
    },
    # 여기에 나머지 7개 유형도 동일한 형식으로 이어서 넣을 수 있습니다.
    # 예시에서는 일부 생략하고 구조만 유지했어요.
}

# Streamlit 앱
st.title("🧠 MBTI 성격유형 분석")
st.markdown("MBTI 유형을 입력하면, 성격 특징과 장점, 단점, 추천 직업, 유명 인물까지 알려드려요!")

# 사용자 입력
user_input = st.text_input("👉 당신의 MBTI를 입력하세요 (예: INFP)").upper()

# 결과 출력
if user_input:
    if user_input in mbti_details:
        info = mbti_details[user_input]
        st.subheader(info["title"])
        st.markdown(f"**📌 성격 요약**\n\n{info['desc']}")
        st.markdown(f"**✅ 강점:** {info['strengths']}")
        st.markdown(f"**⚠️ 약점:** {info['weaknesses']}")
        st.markdown(f"**💼 추천 직업:** {info['jobs']}")
        st.markdown(f"**🌟 유명 인물:** {info['famous']}")
    else:
        st.error("⚠️ 올바른 MBTI를 입력해주세요 (예: INTP, ENFP 등).")
