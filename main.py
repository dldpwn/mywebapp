import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="🩸 ABO/Rh 혈액형 수혈 및 헌혈 가이드",
    page_icon="🩸",
    layout="centered"
)

# 메인 타이틀 및 소개
st.title("🩸 ABO/Rh 혈액형 수혈 & 헌혈 가이드")
st.write("혈액형을 선택하시면 수혈/헌혈 호환 정보와 안전한 헌혈을 위한 유의사항을 확인하실 수 있습니다.")

st.write("---")

# 입력 섹션 (ABO 및 Rh 선택)
col1, col2 = st.columns(2)

with col1:
    rh_factor = st.radio("✨ Rh 식별", ["Rh+", "Rh-"])

with col2:
    abo_type = st.selectbox("✨ ABO 혈액형 선택", ["선택해주세요", "A형", "B형", "O형", "AB형"])

st.write("---")

# 정보 데이터 정의 (전혈 기준 일반적인 수혈 호환성)
# 수혈받을 수 있는 혈액형(적혈구 기준), 헌혈해 줄 수 있는 혈액형
compatibility_data = {
    "Rh+ A형": {
        "receive": ["Rh+ A형", "Rh- A형", "Rh+ O형", "Rh- O형"],
        "give": ["Rh+ A형", "Rh+ AB형"]
    },
    "Rh+ B형": {
        "receive": ["Rh+ B형", "Rh- B형", "Rh+ O형", "Rh- O형"],
        "give": ["Rh+ B형", "Rh+ AB형"]
    },
    "Rh+ O형": {
        "receive": ["Rh+ O형", "Rh- O형"],
        "give": ["Rh+ A형", "Rh+ B형", "Rh+ O형", "Rh+ AB형"]
    },
    "Rh+ AB형": {
        "receive": ["모든 ABO/Rh 혈액형 (Rh+, Rh- A/B/O/AB)"],
        "give": ["Rh+ AB형"]
    },
    "Rh- A형": {
        "receive": ["Rh- A형", "Rh- O형"],
        "give": ["Rh+ A형", "Rh- A형", "Rh+ AB형", "Rh- AB형"]
    },
    "Rh- B형": {
        "receive": ["Rh- B형", "Rh- O형"],
        "give": ["Rh+ B형", "Rh- B형", "Rh+ AB형", "Rh- AB형"]
    },
    "Rh- O형": {
        "receive": ["Rh- O형"],
        "give": ["모든 ABO/Rh 혈액형 (적혈구 공통 가능)"]
    },
    "Rh- AB형": {
        "receive": ["Rh- A형", "Rh- B형", "Rh- O형", "Rh- AB형"],
        "give": ["Rh+ AB형", "Rh- AB형"]
    }
}

# 결과 출력
if abo_type != "선택해주세요":
    full_type = f"{rh_factor} {abo_type}"
    st.subheader(f"📌 [{full_type}] 수혈 및 헌혈 가능 정보")
    
    info = compatibility_data.get(full_type)
    
    col_rec, col_give = st.columns(2)
    
    with col_rec:
        st.info("💉 **수혈받을 수 있는 혈액형**")
        for item in info["receive"]:
            st.write(f"- {item}")
            
    with col_give:
        st.success("🎁 **헌혈해 줄 수 있는 대상 혈액형**")
        for item in info["give"]:
            st.write(f"- {item}")
            
    st.write("---")

# 헌혈 시 유의사항 섹션 (항상 표시 또는 조건부 표시)
st.subheader("📋 안전한 헌혈을 위한 주요 유의사항")

tab1, tab2, tab3 = st.tabs(["헌혈 전 확인사항", "헌혈 당일 유의사항", "헌혈 후 주의사항"])

with tab1:
    st.markdown("""
    * **연령 및 체중 기준**
      * 전혈 헌혈: 만 16세 ~ 69세 (체중: 남성 50kg 이상, 여성 45kg 이상)
      * 성분 헌혈: 만 17세 ~ 69세
    * **신분증 지참**: 주민등록증, 운전면허증, 여권 등 사진과 주민등록번호가 확인되는 신분증 필수.
    * **약물 복용 및 치료**: 치료 목적의 약물 복용(항생제, 여드름 치료제 등)이나 침술/문신 시술 후 일정 기간 헌혈이 제한될 수 있습니다.
    """)

with tab2:
    st.markdown("""
    * **충분한 수분 섭취**: 헌혈 전 물을 충분히 마셔주세요.
    * **식사 필수**: 금식 상태에서는 헌혈이 불가능하므로 꼭 식사를 하고 방문해 주세요.
    * **음주 및 과로 금지**: 헌혈 전날 과음이나 심한 피로는 피해야 합니다.
    """)

with tab3:
    st.markdown("""
    * **충분한 휴식**: 헌혈 직후 헌혈 장소에서 최소 15분 이상 휴식을 취하세요.
    * **수분 보충**: 헌혈 후 평소보다 물을 많이 섭취해 주세요.
    * **격렬한 운동 자제**: 헌혈 당일 심한 운동, 과도한 음주, 사우나 이용은 피하셔야 합니다.
    * **운전 및 작업 주의**: 헌혈 후 어지러움이 느꼈을 때는 즉시 주저앉아 휴식을 취해야 합니다.
    """)

st.write("---")
st.caption("⚠️ **안내**: 본 정보는 일반적인 적혈구 제제 기준 호환 정보이며, 실제 의료 현장에서는 환자의 상태 및 성분제제(백혈구, 혈장 등)에 따라 세부적인 교차시험 후 수혈이 결정됩니다.")
