import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="🩸 레드커넥트 스타일 스마트 헌혈 & 수혈 가이드",
    page_icon="💉",
    layout="centered"
)

# 메인 타이틀
st.title("🩸 스마트 헌혈 자격진단 & 수혈 가이드")
st.caption("레드커넥트 전자문진 기준을 바탕으로 제작된 헌혈 자격 체크 및 수혈 호환성 안내 앱입니다.")

st.write("---")

# 탭 구성
tab_check, tab_compat, tab_notice = st.tabs(["📋 헌혈 가능 자가진단", "🧬 혈액형 수혈 호환", "💡 헌혈 유의사항"])

# ---------------------------------------------------------
# TAB 1: 헌혈 가능 자가진단 (약물, 해외여행, 시술 등)
# ---------------------------------------------------------
with tab_check:
    st.subheader("🔍 헌혈 전 자가 체크리스트")
    st.write("최근 일정, 약물 복용 여부, 시술 이력 등을 선택하여 헌혈 가능 여부를 확인하세요.")

    with st.form("blood_donation_check"):
        # 1. 기본 조건
        st.markdown("### 1. 기본 조건")
        col_age, col_gender, col_weight = st.columns(3)
        with col_age:
            age = st.number_input("만 나이", min_value=10, max_value=100, value=25)
        with col_gender:
            gender = st.selectbox("성별", ["남성", "여성"])
        with col_weight:
            weight = st.number_input("체중 (kg)", min_value=30, max_value=150, value=65)

        st.write("---")

        # 2. 약물 복용 이력
        st.markdown("### 2. 약물 복용 및 주사 이력")
        medication = st.multiselect(
            "최근 복용했거나 주사를 맞은 약물이 있다면 선택하세요.",
            [
                "없음",
                "감기약 / 해열진통제 (최근 3일 이내)",
                "아스피린 (최근 3일 이내)",
                "항생제 / 스테로이드 / 보톡스 (최근 1주일 이내)",
                "여드름 치료제 (이소트레티노인 - 최근 4주 이내)",
                "탈모 치료제 / 전립선비대증 약 (피나스테라이드 - 최근 4주 이내)",
                "전립선비대증 약 (두타스테라이드 - 최근 6개월 이내)",
                "건선 치료제 (아시트레틴 - 최근 3년 이내 / 영구)"
            ],
            default=["없음"]
        )

        st.write("---")

        # 3. 최근 시술 및 해외여행
        st.markdown("### 3. 최근 시술, 해외여행 및 기타 조건")
        
        col_proc, col_travel = st.columns(2)
        with col_proc:
            procedure = st.selectbox(
                "최근 시술/검사 이력",
                [
                    "없음",
                    "예방접종 (독감 등 - 24시간 이내)",
                    "내시경 검사 (최근 4주 이내)",
                    "침술 / 부항(사혈) / 피어싱 (최근 6개월 이내)",
                    "문신 / 타투 (최근 6개월~1년 이내)",
                    "수혈 받음 (최근 1년 이내)"
                ]
            )
        
        with col_travel:
            travel = st.selectbox(
                "최근 해외 방문 이력",
                [
                    "없음 (국내 체류)",
                    "최근 4주 이내 해외 방문/귀국",
                    "말라리아 제한 지역 숙박/거주 이력"
                ]
            )

        submit_button = st.form_submit_button("🩺 헌혈 자격 결과 확인")

    # 진단 결과 로직
    if submit_button:
        st.write("---")
        st.subheader("📊 판정 결과")
        
        disqualifications = []
        warnings = []

        # 1. 체중/나이 검사
        if age < 16 or age > 69:
            disqualifications.append("연령 기준 미달 또는 초과 (전혈 기준 만 16세~69세 가능)")
        
        if gender == "남성" and weight < 50:
            disqualifications.append("남성 체중 기준 미달 (50kg 이상 필요)")
        elif gender == "여성" and weight < 45:
            disqualifications.append("여성 체중 기준 미달 (45kg 이상 필요)")

        # 2. 약물 검사
        if "감기약 / 해열진통제 (최근 3일 이내)" in medication or "아스피린 (최근 3일 이내)" in medication:
            warnings.append("감기약/아스피린/진통제 복용 후 최소 3일이 경과해야 전혈/성분 헌혈이 가능합니다.")
        
        if "항생제 / 스테로이드 / 보톡스 (최근 1주일 이내)" in medication:
            warnings.append("항생제, 스테로이드제, 보톡스 주사 맞은 후 최소 1주일이 경과해야 합니다.")
            
        if "여드름 치료제 (이소트레티노인 - 최근 4주 이내)" in medication or "탈모 치료제 / 전립선비대증 약 (피나스테라이드 - 최근 4주 이내)" in medication:
            disqualifications.append("여드름/탈모 치료제(이소트레티노인, 피나스테라이드) 복용 후 최소 4주간 헌혈 불가")

        if "전립선비대증 약 (두타스테라이드 - 최근 6개월 이내)" in medication:
            disqualifications.append("전립선비대증 치료제(두타스테라이드 - 아보다트 등) 복용 후 최소 6개월간 헌혈 불가")

        if "건선 치료제 (아시트레틴 - 최근 3년 이내 / 영구)" in medication:
            disqualifications.append("건선 치료제 복용 이력이 있는 경우 복용약 성분에 따라 3년~영구 헌혈 금지 대상")

        # 3. 시술 및 해외여행 검사
        if procedure == "예방접종 (독감 등 - 24시간 이내)":
            warnings.append("독감 등 예방접종 후 24시간이 경과해야 헌혈이 가능합니다.")
        elif procedure == "내시경 검사 (최근 4주 이내)":
            warnings.append("내시경 검사 시행 후 최소 4주가 경과해야 합니다.")
        elif procedure == "침술 / 부항(사혈) / 피어싱 (최근 6개월 이내)":
            warnings.append("비의료기관 시술/사혈부항/귀뚫음 등은 최소 6개월간 헌혈이 제한됩니다.")
        elif procedure == "문신 / 타투 (최근 6개월~1년 이내)":
            disqualifications.append("문신/타투 시술 후 최소 6개월~1년간 감염 예방을 위해 헌혈 불가")
        elif procedure == "수혈 받음 (최근 1년 이내)":
            disqualifications.append("수혈을 받은 경우 1년 동안 헌혈이 제한됩니다.")

        if travel == "최근 4주 이내 해외 방문/귀국":
            disqualifications.append("해외 입국 후 최소 4주(28일)간 헌혈 제한")
        elif travel == "말라리아 제한 지역 숙박/거주 이력":
            warnings.append("말라리아 제한지역 방문 시 거주 기간에 따라 전혈이 제한되고 혈장 성분헌혈만 가능할 수 있습니다.")

        # 최종 판정 출력
        if not disqualifications and not warnings:
            st.success("🎉 **헌혈 참여가 가능해 보입니다!** (헌혈의집 방문 시 문진 간호사와 상의 후 최종 확정됩니다.)")
        else:
            if disqualifications:
                st.error("❌ **현재 조건으로는 헌혈 참여가 어렵습니다.**")
                for reason in disqualifications:
                    st.write(f"- {reason}")
            
            if warnings:
                st.warning("⚠️ **주의 및 보류 항목이 있습니다.**")
                for item in warnings:
                    st.write(f"- {item}")


# ---------------------------------------------------------
# TAB 2: ABO/Rh 수혈 호환성
# ---------------------------------------------------------
with tab_compat:
    st.subheader("🧬 ABO 및 Rh 혈액형 수혈 호환성")
    st.write("혈액형별로 수혈을 받을 수 있는 대상과 헌혈을 해줄 수 있는 대상을 조회합니다.")

    col1, col2 = st.columns(2)
    with col1:
        rh_factor = st.radio("Rh 타입", ["Rh+", "Rh-"])
    with col2:
        abo_type = st.selectbox("ABO 타입", ["A형", "B형", "O형", "AB형"])

    full_type = f"{rh_factor} {abo_type}"

    compatibility_data = {
        "Rh+ A형": {"receive": ["Rh+ A형", "Rh- A형", "Rh+ O형", "Rh- O형"], "give": ["Rh+ A형", "Rh+ AB형"]},
        "Rh+ B형": {"receive": ["Rh+ B형", "Rh- B형", "Rh+ O형", "Rh- O형"], "give": ["Rh+ B형", "Rh+ AB형"]},
        "Rh+ O형": {"receive": ["Rh+ O형", "Rh- O형"], "give": ["Rh+ A형", "Rh+ B형", "Rh+ O형", "Rh+ AB형"]},
        "Rh+ AB형": {"receive": ["모든 ABO/Rh 혈액형 (Rh+, Rh- A/B/O/AB)"], "give": ["Rh+ AB형"]},
        "Rh- A형": {"receive": ["Rh- A형", "Rh- O형"], "give": ["Rh+ A형", "Rh- A형", "Rh+ AB형", "Rh- AB형"]},
        "Rh- B형": {"receive": ["Rh- B형", "Rh- O형"], "give": ["Rh+ B형", "Rh- B형", "Rh+ AB형", "Rh- AB형"]},
        "Rh- O형": {"receive": ["Rh- O형"], "give": ["모든 ABO/Rh 혈액형 (적혈구 공통)"]},
        "Rh- AB형": {"receive": ["Rh- A형", "Rh- B형", "Rh- O형", "Rh- AB형"], "give": ["Rh+ AB형", "Rh- AB형"]}
    }

    info = compatibility_data.get(full_type)
    
    st.write("---")
    st.markdown(f"#### 📌 [{full_type}] 호환성 결과")
    
    c_rec, c_give = st.columns(2)
    with c_rec:
        st.info("💉 **수혈받을 수 있는 혈액형**")
        for r in info["receive"]:
            st.write(f"- {r}")
            
    with c_give:
        st.success("🎁 **헌혈해 줄 수 있는 대상 혈액형**")
        for g in info["give"]:
            st.write(f"- {g}")


# ---------------------------------------------------------
# TAB 3: 헌혈 유의사항 (레드커넥트 가이드 기준)
# ---------------------------------------------------------
with tab_notice:
    st.subheader("💡 안전한 헌혈을 위한 사전/사후 가이드")
    
    col_pre, col_post = st.columns(2)
    
    with col_pre:
        st.markdown("#### 🟢 헌혈 전 유의사항")
        st.markdown("""
        * **신분증 필수**: 주민등록증, 운전면허증, 여권, 레드커넥트 앱 모바일 신분증 등
        * **식사 필수**: 공복 상태 헌혈 금지 (최소 헌혈 전 식사 완료)
        * **수분 섭취**: 헌혈 전 물 2컵 이상 충분히 마시기
        * **숙면 및 금주**: 전날 최소 6시간 이상 숙면, 전날 음주 자제
        """)
        
    with col_post:
        st.markdown("#### 🔴 헌혈 후 유의사항")
        st.markdown("""
        * **휴식**: 헌혈 직후 현장에서 최소 15분 이상 휴식
        * **지혈**: 헌혈 부위 반창고는 최소 4시간 이상 부착 및 문지르지 말 것
        * **수분 공급**: 평소보다 물을 3~4컵 더 마시기
        * **주의사항**:
          - 당일 음주, 흡연, 격렬한 운동, 사우나 금지
          - 어지러움 발생 시 즉시 주저앉아 머리를 낮추기
        """)

st.write("---")
st.caption("⚠️ **안내**: 본 진단 프로그램은 참조용으로 제작되었으며, 실제 헌혈 가능 여부는 헌혈 현장에서 문진간호사와의 최종 상담 결과에 따라 결정됩니다.")
