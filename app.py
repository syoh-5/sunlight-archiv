import streamlit as st
import os
import base64

# 1. 사이트 기본 설정
st.set_page_config(page_title="도민발전소 자료모음", layout="wide")

# 2. 보안
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

# PDF 뷰어 함수
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'''
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="800px" 
            type="application/pdf">
        </iframe>
    '''
    st.markdown(pdf_display, unsafe_allow_html=True)

# 3. 본문
st.title("☀️ 도민발전소 자료모음")

tabs = st.tabs(["📋 기획안", "📈 수익성 분석", "🤝 협동조합", "📡 입찰시나리오", "📝 법령"])

# --- 탭 1: 기획안 ---
with tabs[0]:
    st.header("📋 기획안")
    st.write("조회할 파일을 선택하세요.")

    proposal_files = sorted([f for f in os.listdir('proposals') if f.endswith('.pdf')])

    if proposal_files:
        selected = st.selectbox("📄 파일 선택", proposal_files, key="proposal_select")
        if selected:
            show_pdf(os.path.join('proposals', selected))
    else:
        st.info("현재 업로드된 기획안이 없습니다.")

# --- 탭 2: 수익성 분석 ---
with tabs[1]:
    st.header("📈 재무적 수익성 분석")
    st.info("수익 시뮬레이션 사이트 및 관련 자료가 업데이트될 예정입니다.")

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

# --- 탭 5: 법령 ---
with tabs[4]:
    st.header("📝 법령검토")
    st.write("조회할 법령을 선택하세요.")

    law_files = sorted([f for f in os.listdir('laws') if f.endswith('.pdf')])

    if law_files:
        selected_law = st.selectbox("📄 파일 선택", law_files, key="law_select")
        if selected_law:
            show_pdf(os.path.join('laws', selected_law))
    else:
        st.info("업로드된 법령 자료가 없습니다.")
