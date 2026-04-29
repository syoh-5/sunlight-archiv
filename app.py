import streamlit as st
import os

# 1. 사이트 기본 설정
st.set_page_config(page_title="도민발전소 통합 플랫폼", layout="wide")

# 스타일 설정 (카드 색상을 연하고 부드럽게 변경)
st.markdown("""
    <style>
    .stDownloadButton {
        width: 100%;
    }
    .stDownloadButton button {
        width: 100%;
        height: 70px;
        background-color: #f8f9fa; /* 아주 연한 회색 배경 */
        color: #495057; /* 진한 회색 글자 */
        border-radius: 12px;
        border: 1px solid #dee2e6; /* 연한 테두리 */
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }
    /* 마우스를 올렸을 때(Hover) 효과 */
    .stDownloadButton button:hover {
        background-color: #ffffff; /* 배경이 하얗게 변함 */
        color: #007BFF; /* 글자색은 파란색으로 포인트 */
        border: 1px solid #007BFF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05); /* 살짝 떠오르는 느낌 */
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 보안 (비밀번호 설정)
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🔒 보안 접속")
    pw = st.text_input("비밀번호를 입력하세요", type="password")
    if pw == "1234":
        st.session_state["password_correct"] = True
        st.rerun()
    else:
        st.stop()

# 3. 본문 시작
st.title("☀️ 도민발전소 통합 관리 플랫폼")

# 탭 구성 (수연 님 요청 순서 그대로)
tabs = st.tabs(["⚖️ 법령검토", "📈 수익성 분석", "🤝 협동조합", "📡 입찰시나리오", "📝 기획안"])

# --- 탭 1: 법령검토 ---
with tabs[0]:
    st.header("⚖️ 관련 법령 리스트")
    st.write("조회(다운로드)할 법령을 클릭하세요.")
    
    pdf_files = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
    
    if pdf_files:
        cols = st.columns(3)
        for i, file_name in enumerate(pdf_files):
            with cols[i % 3]:
                with open(file_name, "rb") as f:
                    st.download_button(
                        label=f"📄 {file_name}",
                        data=f,
                        file_name=file_name,
                        mime="application/pdf",
                        key=f"btn_{i}"
                    )
    else:
        st.info("현재 업로드된 법령 자료가 없습니다.")

# --- 탭 2: 수익성 분석 ---
with tabs[1]:
    st.header("📈 재무적 수익성 분석")
    st.info("수익 시뮬레이션 및 데이터 자료가 업데이트될 예정입니다.")
    
# --- 탭 3: 협동조합 ---
with tabs[2]:
    st.header("🤝 협동조합 거버넌스")
    with st.expander("📌 조합 설립 관련 자료"):
        st.write("- 표준 정관 안")
        st.write("- 조합원 모집 가이드")

# --- 탭 4: 입찰시나리오 ---
with tabs[3]:
    st.header("📡 시나리오 ABC분석")
    st.warning("분석 데이터가 들어갈 예정입니다.")

# --- 탭 5: 기획안 ---
with tabs[4]:
    st.header("📝 사업 기획 및 제안서")
    plan_files = sorted([f for f in os.listdir('.') if f.endswith('.pdf')])
    
    if plan_files:
        cols_plan = st.columns(2)
        for i, file_name in enumerate(plan_files):
            with cols_plan[i % 2]:
                with open(file_name, "rb") as f:
                    st.download_button(
                        label=f"📁 {file_name}",
                        data=f,
                        file_name=file_name,
                        mime="application/pdf",
                        key=f"plan_btn_{i}"
                    )
    else:
        st.info("업로드된 기획안이 없습니다.")
