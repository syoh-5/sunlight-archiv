import streamlit as st
import os
import base64

# 1. 사이트 기본 설정
st.set_page_config(page_title="도민발전소 통합 플랫폼", layout="wide")

# PDF를 새 창에서 열기 위한 함수 (Base64 인코딩 방식 유지)
def get_pdf_display_link(file_path, link_text):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # 버튼처럼 보이는 스타일의 링크 생성
    href = f'<a href="data:application/pdf;base64,{base64_pdf}" target="_blank" style="text-decoration: none; display: inline-block; padding: 10px 15px; background-color: #007BFF; color: white; border-radius: 8px; font-weight: bold; margin: 5px;">{link_text}</a>'
    return href

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

# 탭 구성 (수연 님 요청 순서)
tabs = st.tabs(["⚖️ 법령검토", "📈 수익성 분석", "🤝 협동조합", "📡 입찰시나리오", "📝 기획안"])

# --- 탭 1: 법령검토 (목록 나열 방식) ---
with tabs[0]:
    st.header("⚖️ 관련 법령 리스트")
    st.write("조회하고 싶은 법령의 버튼을 클릭하면 새 탭에서 열립니다.")
    
    pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if pdf_files:
        # 파일을 3개씩 가로로 나열
        cols = st.columns(3)
        for i, file_name in enumerate(pdf_files):
            with cols[i % 3]:
                st.markdown(get_pdf_display_link(file_name, f"📄 {file_name}"), unsafe_allow_html=True)
                st.caption(f"크기: {os.path.getsize(file_name)//1024} KB")
    else:
        st.info("현재 업로드된 법령 자료가 없습니다.")

# --- 탭 2: 수익성 분석 ---
with tabs[1]:
    st.header("📈 재무적 수익성 분석")
    st.info("추후 만들어지는 수익 시뮬 사이트와 자료가 들어갈 예정입니다.")
    
# --- 탭 3: 협동조합 ---
with tabs[2]:
    st.header("🤝 협동조합 거버넌스")
    with st.expander("📌 조합 설립 관련 자료"):
        st.markdown("- 표준 정관 안\n- 조합원 모집 공고문")

# --- 탭 4: 입찰시나리오 ---
with tabs[3]:
    st.header("📡 시나리오 ABC분석")
    st.warning("분석 파일 및 데이터 대시보드가 들어갈 예정입니다.")

# --- 탭 5: 기획안 (목록 나열 방식) ---
with tabs[4]:
    st.header("📝 사업 기획 및 제안서")
    plan_files = [f for f in os.listdir('.') if f.endswith('.pdf')]
    
    if plan_files:
        # 기획안도 보기 좋게 열별로 나열
        cols_plan = st.columns(2)
        for i, file_name in enumerate(plan_files):
            with cols_plan[i % 2]:
                st.markdown(get_pdf_display_link(file_name, f"📁 {file_name}"), unsafe_allow_html=True)
    else:
        st.info("업로드된 기획안이 없습니다.")
