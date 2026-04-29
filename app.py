import streamlit as st
import os
import base64

# 1. 사이트 기본 설정
st.set_page_config(page_title="도민발전소 통합 플랫폼", layout="wide")

# PDF를 화면에 바로 띄우는 함수
def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # iframe을 사용하여 PDF 뷰어 삽입
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# 2. 보안 (비밀번호 설정)
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🔒 보안 접속")
    pw = st.text_input("비밀번호를 입력하세요", type="password")
    if pw == "1234": # 원하는 비밀번호로 수정하세요
        st.session_state["password_correct"] = True
        st.rerun()
    else:
        st.stop()

# 3. 본문 시작 (비밀번호 통과 시)
st.title("☀️ 도민발전소 통합 관리 플랫폼")

# 요청하신 탭 구성 (수익성 분석이 두 번 들어가 있어서 하나로 합치거나 순서를 조정했습니다)
tabs = st.tabs(["⚖️ 법령검토", "📈 수익성 분석", "🤝 협동조합", "📡 입찰시나리오", "📝 기획안"])

# --- 탭 1: 법령검토 ---
with tabs[0]:
    st.header("법령 및 지침 검토")
    st.write("관련 법령 PDF를 선택하면 아래에서 바로 조회할 수 있습니다.")
    
    # 현재 폴더에 있는 PDF 파일 목록 가져오기
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if pdf_files:
        selected_file = st.selectbox("조회할 법령 파일을 선택하세요", pdf_files, key="tab1_select")
        if st.button("파일 열기", key="tab1_btn"):
            display_pdf(selected_file)
    else:
        st.info("아직 업로드된 법령 PDF 파일이 없습니다.")

# --- 탭 2: 수익성 분석 ---
with tabs[1]:
    st.header("재무적 수익성 분석")
    st.subheader("사이트")
    st.info("추후 만들어지는 수익 시뮬 사이트와 자료가 들어갈 예정입니다.")
    
# --- 탭 3: 협동조합 ---
with tabs[2]:
    st.header("협동조합 거버넌스")
    st.write("조합원 명부, 정관, 이익 배분 가이드라인을 관리합니다.")
    # 하위 파일 관리 (접이식 메뉴)
    with st.expander("조합 설립 관련 자료"):
        st.markdown("- 표준 정관 안\n- 조합원 모집 공고문")

# --- 탭 4: 입찰시나리오 ---
with tabs[3]:
    st.header("시나리오 ABC분석")
    st.write("입찰시나리오 분석.")
    st.warning("분석파일이 들어갈예정입니다.")

# --- 탭 5: 기획안 ---
with tabs[4]:
    st.header("사업 기획 및 제안서")
    # 기획안 PDF 조회 기능
    pdf_files_plan = [f for f in os.listdir('.') if f.endswith('.pdf')]
    if pdf_files_plan:
        selected_plan = st.selectbox("조회할 기획안을 선택하세요", pdf_files_plan, key="tab5_select")
        if st.button("기획안 보기", key="tab5_btn"):
            display_pdf(selected_plan)
