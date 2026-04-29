import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

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
        pdf_bytes = f.read()
    pdf_viewer(pdf_bytes)

# 카드형 파일 선택 함수
def file_card_selector(files, folder, session_key):
    if session_key not in st.session_state:
        st.session_state[session_key] = None

    cols = st.columns(3)
    for i, file_name in enumerate(files):
        with cols[i % 3]:
            is_selected = st.session_state[session_key] == file_name
            label = f"{'✅' if is_selected else '📄'} {file_name.replace('.pdf', '')}"
            if st.button(label, key=f"{session_key}_{i}", use_container_width=True):
                st.session_state[session_key] = file_name
                st.rerun()

    if st.session_state[session_key]:
        st.divider()
        st.markdown(f"**📖 현재 보는 파일:** `{st.session_state[session_key]}`")
        show_pdf(os.path.join(folder, st.session_state[session_key]))

# 3. 본문
st.title("☀️ 도민발전소 자료모음")

tabs = st.tabs(["📋 기획안", "📈 수익분석", "🤝 협동조합", "📡 입찰시나리오", "📝 법령"])

# --- 탭 1: 기획안 ---
with tabs[0]:
    st.header("📋 기획안")
    st.caption("파일을 클릭하면 바로 아래에 열립니다.")
    proposal_files = sorted([f for f in os.listdir('proposals') if f.endswith('.pdf')])
    if proposal_files:
        file_card_selector(proposal_files, 'proposals', 'selected_proposal')
    else:
        st.info("현재 업로드된 기획안이 없습니다.")

# --- 탭 2: 수익분석 ---
with tabs[1]:
    st.header("📈 수익분석")

    st.subheader("🔗 관련 사이트")
    st.markdown("""
    - [수익분석](추가예정~~)
    """)

    st.divider()

    st.subheader("📰 관련 기사")

    articles = [
        {
            "title": "PPA",
            "source": "",
            "date": "",
            "url": "https://https://www.lawtimes.co.kr/news/articleView.html?idxno=217995&utm_source=chatgpt.com"
        },
        {
            "title": "두번째 기사 제목",
            "source": "출처 (예: 경향신문)",
            "date": "2025.03.15",
            "url": "https://기사링크주소"
        },
    ]

    for article in articles:
        with st.container(border=True):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.markdown(f"**{article['title']}**")
                st.caption(f"📰 {article['source']} · {article['date']}")
            with col2:
                st.link_button("기사 보기 →", article['url'])

# --- 탭 3: 협동조합 ---
with tabs[2]:
    st.header("🤝 협동조합 거버넌스")
    with st.expander("📌 조합 설립 관련 자료"):
        st.write("- 표준 정관 안")
        st.write("- 조합원 모집 가이드")

    st.divider()
    st.subheader("🖼️ 협동조합 자료 갤러리")

    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    if os.path.exists('images'):
        image_files = sorted([
            f for f in os.listdir('images')
            if f.lower().endswith(image_extensions)
        ])
        if image_files:
            cols = st.columns(3)
            for i, img_file in enumerate(image_files):
                with cols[i % 3]:
                    st.image(
                        os.path.join('images', img_file),
                        caption=img_file.rsplit('.', 1)[0],
                        use_container_width=True
                    )
        else:
            st.info("현재 업로드된 이미지가 없습니다.")
    else:
        st.info("images 폴더가 없습니다.")

# --- 탭 4: 입찰시나리오 ---
with tabs[3]:
    st.header("📡 시나리오 ABC분석")
    st.warning("분석 데이터가 들어갈 예정입니다.")

# --- 탭 5: 법령 ---
with tabs[4]:
    st.header("📝 법령검토")
    st.caption("파일을 클릭하면 바로 아래에 열립니다.")
    law_files = sorted([f for f in os.listdir('laws') if f.endswith('.pdf')])
    if law_files:
        file_card_selector(law_files, 'laws', 'selected_law')
    else:
        st.info("업로드된 법령 자료가 없습니다.")
