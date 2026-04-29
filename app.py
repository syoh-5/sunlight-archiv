import streamlit as st

# 사이트 기본 설정
st.set_page_config(page_title="도민발전소 아카이브", layout="wide")

# 제목
st.title("☀️ 도민발전소 자료 및 법령실")
st.write("관련 자료를 정리하는 공간입니다.")

# 탭 메뉴 만들기
tab1, tab2 = st.tabs(["📄 주요 자료실", "⚖️ 검토 법령"])

with tab1:
    st.header("도민발전소 관련 자료")
    st.info("GitHub에 올린 PDF 파일들을 여기서 다운로드할 수 있습니다.")
    
    # PDF 다운로드 버튼 (파일명을 나중에 올리신 파일명으로 수정하시면 됩니다)
    # 현재는 예시로 'roadmap.pdf'라고 적어두었습니다.
    try:
        with open("roadmap.pdf", "rb") as f:
            st.download_button("📂 도민발전소 로드맵 다운로드", f, file_name="roadmap.pdf")
    except:
        st.warning("아직 PDF 파일이 업로드되지 않았거나 파일명이 다릅니다. GitHub에 PDF를 올린 후 파일명을 맞춰주세요!")

with tab2:
    st.header("주요 검토 법령 및 지침")
    st.markdown("""
    업무 시 상시 확인해야 할 법령 리스트입니다.
