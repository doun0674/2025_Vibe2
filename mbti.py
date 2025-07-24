import streamlit as st

# 16가지 MBTI 상세 설명
mbti_details = {
    "ISTJ": {
        "title": "🧱 ISTJ - 현실주의자형",
        "desc": "신중하고 책임감 있으며 체계적인 성격으로, 전통과 규칙을 중시합니다.",
        "strengths": "성실함, 조직력, 철저한 계획",
        "weaknesses": "융통성 부족, 감정 표현 어려움",
        "jobs": "공무원, 회계사, 엔지니어, 군인",
        "famous": "나폴레옹, 제프 베조스"
    },
    "ISFJ": {
        "title": "🛡️ ISFJ - 수호자형",
        "desc": "조용하지만 따뜻하고 헌신적인 성격으로, 타인을 돕고자 하는 마음이 큽니다.",
        "strengths": "헌신성, 배려심, 책임감",
        "weaknesses": "비판에 민감, 자기 표현 부족",
        "jobs": "간호사, 교사, 사회복지사",
        "famous": "비욘세, 케이트 미들턴"
    },
    "INFJ": {
        "title": "🌌 INFJ - 옹호자형",
        "desc": "이상과 신념을 중요시하며 조용하고 직관적인 사고로 세상을 바꾸려 합니다.",
        "strengths": "직관력, 공감 능력, 깊은 사고",
        "weaknesses": "완벽주의, 과한 이상 추구",
        "jobs": "상담가, 심리학자, 작가",
        "famous": "마틴 루터 킹 주니어, 넬슨 만델라"
    },
    "INTJ": {
        "title": "🔮 INTJ - 전략가형",
        "desc": "논리적이고 분석적인 전략가로, 독립적으로 일하고 장기적인 목표를 추구합니다.",
        "strengths": "계획성, 독창성, 자기주도",
        "weaknesses": "감정 무시, 융통성 부족",
        "jobs": "과학자, 엔지니어, 전략기획자",
        "famous": "일론 머스크, 니콜라 테슬라"
    },
    "ISTP": {
        "title": "🛠️ ISTP - 장인형",
        "desc": "실용적이고 논리적인 문제 해결사로, 독립적이고 조용한 편입니다.",
        "strengths": "적응력, 분석력, 독립심",
        "weaknesses": "감정 표현 어려움, 충동적",
        "jobs": "엔지니어, 정비사, 파일럿",
        "famous": "클린트 이스트우드, 마이클 조던"
    },
    "ISFP": {
        "title": "🎨 ISFP - 모험가형",
        "desc": "조용하고 온화하며 감성적인 예술가로, 자유와 개성을 중요시합니다.",
        "strengths": "유연성, 감성, 충성심",
        "weaknesses": "우유부단, 자기 주장 부족",
        "jobs": "예술가, 디자이너, 셰프",
        "famous": "마이클 잭슨, 프린스"
    },
    "INFP": {
        "title": "🌷 INFP - 중재자형",
        "desc": "이상주의적이고 내면의 가치에 충실하며, 창의적이고 공감 능력이 뛰어납니다.",
        "strengths": "이상주의, 창의성, 공감",
        "weaknesses": "현실 회피, 감정 기복",
        "jobs": "작가, 시인, 상담가",
        "famous": "윌리엄 셰익스피어, 조니 뎁"
    },
    "INTP": {
        "title": "🧠 INTP - 논리사고형",
        "desc": "아이디어와 이론에 매료되는 철학자형으로, 분석적이고 창의적인 성격입니다.",
        "strengths": "논리적 사고, 창의성, 독립성",
        "weaknesses": "비현실적, 감정 표현 부족",
        "jobs": "과학자, 개발자, 이론가",
        "famous": "앨버트 아인슈타인, 빌 게이츠"
    },
    "ESTP": {
        "title": "🏎️ ESTP - 사업가형",
        "desc": "에너지가 넘치고 현실적인 사고를 가진 유형으로, 즉흥적인 해결 능력이 뛰어납니다.",
        "strengths": "대담함, 현실감각, 문제 해결력",
        "weaknesses": "충동적, 인내심 부족",
        "jobs": "세일즈, 기업가, 운동선수",
        "famous": "어니스트 헤밍웨이, 브루스 윌리스"
    },
    "ESFP": {
        "title": "🎉 ESFP - 연예인형",
        "desc": "사교적이고 감각적인 유형으로, 사람들과 즐거운 순간을 함께하는 것을 좋아합니다.",
        "strengths": "사교성, 활발함, 낙천성",
        "weaknesses": "계획 부족, 감정적",
        "jobs": "연예인, MC, 이벤트 코디네이터",
        "famous": "엘비스 프레슬리, 마일리 사이러스"
    },
    "ENFP": {
        "title": "🌈 ENFP - 활동가형",
        "desc": "창의적이고 열정적이며, 새로운 경험과 사람과의 연결을 중시합니다.",
        "strengths": "열정, 창의성, 사교성",
        "weaknesses": "산만함, 계획 부족",
        "jobs": "배우, 작가, 마케터",
        "famous": "로빈 윌리엄스, 샤를리즈 테론"
    },
    "ENTP": {
        "title": "⚡ ENTP - 발명가형",
        "desc": "아이디어에 열정적이고 논쟁을 즐기며, 새로운 방식으로 문제를 해결합니다.",
        "strengths": "창의력, 재치, 유연성",
        "weaknesses": "끈기 부족, 규칙 회피",
        "jobs": "변호사, 창업가, 기획자",
        "famous": "마크 트웨인, 톰 행크스"
    },
    "ESTJ": {
        "title": "🏗️ ESTJ - 경영자형",
        "desc": "논리적이고 조직적인 성격으로, 체계적으로 목표를 추진합니다.",
        "strengths": "책임감, 리더십, 현실감",
        "weaknesses": "융통성 부족, 완고함",
        "jobs": "관리자, 군인, 판사",
        "famous": "프랭클린 루스벨트, 존 F. 케네디"
    },
    "ESFJ": {
        "title": "🤝 ESFJ - 집정관형",
        "desc": "타인과의 조화를 중요시하고, 배려심이 많은 사교적 성격입니다.",
        "strengths": "친절함, 협동성, 책임감",
        "weaknesses": "타인의 시선 의식, 변화에 약함",
        "jobs": "간호사, 교사, 고객 서비스",
        "famous": "테일러 스위프트, 휴 그랜트"
    },
    "ENFJ": {
        "title": "📣 ENFJ - 선도자형",
        "desc": "타인을 이끄는 데 능숙하고, 따뜻하며 이상적인 사회 리더입니다.",
        "strengths": "지도력, 공감 능력, 열정",
        "weaknesses": "자기 희생적, 과도한 이상 추구",
        "jobs": "상담사, 교육자, 정치인",
        "famous": "오프라 윈프리, 넬슨 만델라"
    },
    "ENTJ": {
        "title": "👑 ENTJ - 통솔자형",
        "desc": "논리적이고 추진력 있는 리더형으로, 효율성과 목표 달성을 중요시합니다.",
        "strengths": "계획력, 리더십, 전략적 사고",
        "weaknesses": "권위적, 감정 무시",
        "jobs": "CEO, 경영 컨설턴트, 전략가",
        "famous": "스티브 잡스, 고든 램지"
    }
}

# Streamlit 앱 UI
st.title("🧠 MBTI 성격유형 분석기")
st.markdown("16가지 MBTI 유형에 대한 성격, 장단점, 추천 직업, 유명 인물까지 한눈에 확인해보세요!")

# 사용자 입력
user_input = st.text_input("👉 MBTI를 입력하세요 (예: INFP, ENTJ)").upper()

# 결과 출력
if user_input:
    if user_input in mbti_details:
        info = mbti_details[user_input]
        st.subheader(info["title"])
        st.markdown(f"**📌 성격 요약**\n{info['desc']}")
        st.markdown(f"**✅ 강점:** {info['strengths']}")
        st.markdown(f"**⚠️ 약점:** {info['weaknesses']}")
        st.markdown(f"**💼 추천 직업:** {info['jobs']}")
        st.markdown(f"**🌟 유명 인물:** {info['famous']}")
    else:
        st.error("⚠️ 올바른 MBTI를 입력해주세요 (예: ENTP, ISFJ 등).")
