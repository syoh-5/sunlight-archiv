import streamlit as st
import os

# 1. 사이트 기본 설정 및 보안(비밀번호)
st.set_page_config(page_title="도민발전소 아카이브", layout="wide")

def check_password():
    def password_entered():
        if st.session_state["password"] == "1234": # <--- 원하는 비밀번호로 바꾸세요!
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("비밀번호를 입력하세요", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("비밀번호가 틀렸습니다. 다시 입력하세요", type="password", on_change=password_entered, key="password")
        return False
    else:
        return True

if check_password():
    # 2. 본문 내용 (비밀번호 통과 시 보임)
    st.title("☀️ 도민발전소 자료실")
    
    tab1, tab2 = st.tabs(["📄 전체자료확인", "⚖️ 필수 법령"])

    with tab1:
        st.subheader("업로드된 모든 PDF 자료")
        # 폴더 내의 모든 파일을 확인해서 PDF만 버튼으로 자동 생성
        files = [f for f in os.listdir('.') if f.endswith('.pdf')]
        
        if files:
            for file_name in files:
                with open(file_name, "rb") as f:
                    st.download_button(
                        label=f"📂 {file_name}",
                        data=f,
                        file_name=file_name,
                        key=file_name # 버튼마다 고유 키 부여
                    )
        else:
            st.warning("아직 업로드된 PDF 파일이 없습니다.")

    with tab2:
        st.subheader("협동조합 아카이브")
        st.markdown("""
        - **신재생에너지법**: 사업 추진의 법적 근거
        - **분산에너지 활성화 특별법**: VPP 및 지역 에너지 체계의 핵심
        - **전기사업법**: 발전사업 허가 및 전력 거래 관련
        - **경기도 에너지 조례**: 지자체 지원 및 협력 근거
        """)
