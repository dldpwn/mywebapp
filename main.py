import streamlit as st

# 페이지 기본 설정 (타이틀, 파비콘, 레이아웃)
st.set_page_config(
    page_title="💖 MBTI 뽀짝 여행지 추천소 💖",
    page_icon="✈️",
    layout="centered"
)

# 메인 타이틀 및 소개
st.title("💖 MBTI 뽀짝 여행지 추천소 💖")
st.caption("당신의 MBTI를 알려주면 딱 맞는 힐링 여행지를 슝슝 추천해드릴게요! (ฅ^•ﻌ•^ฅ)")

st.write("---")

# MBTI 목록 정의
mbti_list = [
    "선택해주세요!",
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 귀여운 드롭다운 선택 상자
selected_mbti = st.selectbox("✨ 당신의 MBTI를 선택해주세요! ✨", mbti_list)

# MBTI별 추천 여행지 정보 사전
recommendations = {
    "ISTJ": {"place": "🇩🇪 독일 뮌헨", "desc": "계획적이고 차분한 당신! 질서정연하고 역사 깊은 뮌헨에서 완벽한 일정을 즐겨보세요 🏰"},
    "ISFJ": {"place": "🇯🇵 일본 교토", "desc": "따뜻하고 배려심 깊은 당신! 고즈넉한 풍경과 아기자기한 거리에서 힐링해보아요 🍵"},
    "INFJ": {"place": "🇨🇭 스위스 체르마트", "desc": "조용히 깊은 생각에 잠기는 당신! 알프스 산맥의 동화 같은 풍경이 마음을 가득 채워줄 거예요 🏔️"},
    "INTJ": {"place": "🇬🇧 영국 옥스퍼드", "desc": "지적이고 호기심 많은 당신! 고풍스러운 도서관과 지식의 향기가 가득한 곳으로 떠나봐요 📚"},
    "ISTP": {"place": "🇳🇿 뉴질랜드 퀸스타운", "desc": "조용한 액티비티 마니아! 대자연 속에서 즐기는 스릴 만점 익스트림 스포츠 🪂"},
    "ISFP": {"place": "🇮🇹 이탈리아 피렌체", "desc": "다정한 예술가 타입! 골목마다 감성이 넘쳐나는 예술의 도시에서 인생샷 완성 🎨"},
    "INFP": {"place": "🇮🇸 아이슬란드 레이캬비크", "desc": "몽상가이자 낭만파! 밤하늘을 수놓는 오로라를 보며 감성 충전 100% 🌌"},
    "INTP": {"place": "🇪🇬 이집트 카이로", "desc": "호기심 천국 탐구가! 피라미드의 신비를 파헤치는 비밀스러운 여행 🐫"},
    "ESTP": {"place": "🇺🇸 미국 라스베이거스", "desc": "에너지 넘치는 화려한 리더! 잠들지 않는 도시에서 화려한 조명과 쇼를 즐겨요 🎲"},
    "ESFP": {"place": "🇪🇸 스페인 바르셀로나", "desc": "흥 부자 슈퍼스타! 열정적인 음악과 축제, 맛있는 타파스가 기다려요 💃"},
    "ENFP": {"place": "🇹🇭 태국 방콕", "desc": "매일이 새로운 에너자이저! 화려한 야시장과 맛있는 길거리 음식의 천국 🍜"},
    "ENTP": {"place": "🇹🇼 대만 타이베이", "desc": "새로운 것에 끌리는 모험가! 볼거리와 먹거리가 끊이지 않는 독특한 감성 여행 🎈"},
    "ESTJ": {"place": "🇸🇬 싱가포르", "desc": "깔끔하고 완벽함을 추구하는 당신! 체계적이고 쾌적한 도시에서 완벽한 휴식을 🏙️"},
    "ESFJ": {"place": "🇫🇷 프랑스 파리", "desc": "친절하고 사교적인 당신! 낭만이 흐르는 에펠탑 아래에서 사랑하는 사람들과 추억 쌓기 🥐"},
    "ENFJ": {"place": "🇭🇺 헝가리 부다페스트", "desc": "따뜻한 리더십의 소유자! 야경이 아름다운 다뉴브 강가에서 낭만적인 밤을 보내세요 🏰"},
    "ENTJ": {"place": "🇦🇪 아랍에미리트 두바이", "desc": "야망 가득한 멋쟁이! 세계 최고의 높이와 화려함을 자랑하는 럭셔리 여행 🏙️"}
}

# 결과 출력 부분
if selected_mbti != "선택해주세요!":
    st.write("")
    st.success(f"🎉 **{selected_mbti}** 님을 위한 뽀짝 추천 여행지!")
    
    info = recommendations[selected_mbti]
    
    # 귀여운 안내 상자
    st.subheader(f"📍 추천 여행지: {info['place']}")
    st.write(info['desc'])
    
    # 감성 스티커 느낌의 풍선 효과
    st.balloons()
else:
    st.info("👆 위 목록에서 MBTI를 선택해 주세요! (두근두근) 💓")

# 하단 귀여운 푸터
st.write("---")
st.caption("제작: 🐾 세상에서 가장 귀여운 여행 안내원 🐾")
