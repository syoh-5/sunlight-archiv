import streamlit as st
import os
from streamlit_pdf_viewer import pdf_viewer

# ===========================
# 1. 사이트 기본 설정
# ===========================
st.set_page_config(page_title="도민발전소 자료모음", layout="wide")

# ===========================
# 2. 보안
# ===========================
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

# ===========================
# 공통 함수
# ===========================

# PDF 뷰어
def show_pdf(file_path):
    with open(file_path, "rb") as f:
        pdf_bytes = f.read()
    pdf_viewer(pdf_bytes)

# 카드형 파일 선택기 (조회 + 다운로드)
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

        # ✅ 파일명 + 다운로드 버튼 한 줄에
        col_title, col_btn = st.columns([6, 1])
        with col_title:
            st.markdown(f"**📖 현재 보는 파일:** `{st.session_state[session_key]}`")
        with col_btn:
            file_path = os.path.join(folder, st.session_state[session_key])
            with open(file_path, "rb") as f:
                st.download_button(
                    label="⬇️ 저장",
                    data=f,
                    file_name=st.session_state[session_key],
                    mime="application/pdf",
                    key=f"dl_{session_key}",
                    use_container_width=True
                )

        show_pdf(os.path.join(folder, st.session_state[session_key]))

# 이미지 갤러리
def image_gallery(folder):
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    if os.path.exists(folder):
        image_files = sorted([
            f for f in os.listdir(folder)
            if f.lower().endswith(image_extensions)
        ])
        if image_files:
            cols = st.columns(3)
            for i, img_file in enumerate(image_files):
                with cols[i % 3]:
                    st.image(
                        os.path.join(folder, img_file),
                        caption=img_file.rsplit('.', 1)[0],
                        use_container_width=True
                    )
        else:
            st.info("업로드된 이미지가 없습니다.")
    else:
        st.info("폴더가 없습니다. GitHub에 폴더를 생성해주세요.")

# ===========================
# 3. 본문
# ===========================
st.title("☀️ 도민발전소 자료모음")

tabs = st.tabs([
    "📋 기획안",
    "📈 수익분석",
    "🤝 협동조합",
    "📡 입찰시나리오",
    "📝 법령",
    "📂 관련자료"
])

# ===========================
# 탭 1: 기획안
# ===========================
with tabs[0]:
    st.header("📋 기획안")
    st.caption("파일을 클릭하면 바로 아래에서 조회 및 저장할 수 있습니다.")
    proposal_files = sorted([f for f in os.listdir('proposals') if f.endswith('.pdf')])
    if proposal_files:
        file_card_selector(proposal_files, 'proposals', 'selected_proposal')
    else:
        st.info("현재 업로드된 기획안이 없습니다.")

# ===========================
# 탭 2: 수익분석
# ===========================
with tabs[1]:
    st.header("📈 수익분석")

    st.subheader("🔗 관련 사이트")
    st.markdown("""
    - [연계예정](~~~)
    - [연계예정](~~~)
    """)

    st.divider()

    st.subheader("📰 관련 기사")
    articles = [
        {
            "title": "기사 제목을 여기에 입력하세요",
            "source": "출처",
            "date": "2025.04.21",
            "url": "https://기사링크"
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

# ===========================
# 탭 3: 협동조합
# ===========================
with tabs[2]:
    st.header("🤝 협동조합 거버넌스")

    st.subheader("📄 관련 서류")
    st.caption("파일을 클릭하면 바로 아래에서 조회 및 저장할 수 있습니다.")
    coop_files = sorted([f for f in os.listdir('cooperative') if f.endswith('.pdf')]) \
        if os.path.exists('cooperative') else []
    if coop_files:
        file_card_selector(coop_files, 'cooperative', 'selected_coop')
    else:
        st.info("업로드된 서류가 없습니다.")

    st.divider()

    st.subheader("🖼️ 갤러리")
    image_gallery('cooperative_img')

# ===========================
# 탭 4: 입찰시나리오
# ===========================
with tabs[3]:
    st.header("📡 시나리오 ABC분석")
    st.warning("분석 데이터가 들어갈 예정입니다.")

# ===========================
# 탭 5: 법령
# ===========================
with tabs[4]:
    st.header("📝 법령검토")
    st.caption("파일을 클릭하면 바로 아래에서 조회 및 저장할 수 있습니다.")
    law_files = sorted([f for f in os.listdir('laws') if f.endswith('.pdf')])
    if law_files:
        file_card_selector(law_files, 'laws', 'selected_law')
    else:
        st.info("업로드된 법령 자료가 없습니다.")

# ===========================
# 탭 6: 관련자료
# ===========================
with tabs[5]:
    st.header("📂 관련자료")

    st.subheader("🔗 관련 링크")
    st.markdown("""
    - [링크 제목 1](https://링크주소)
    - [링크 제목 2](https://링크주소)
    """)

    st.divider()

    st.subheader("📄 첨부 자료")
    st.caption("파일을 클릭하면 바로 아래에서 조회 및 저장할 수 있습니다.")
    ref_files = sorted([f for f in os.listdir('references') if f.endswith('.pdf')]) \
        if os.path.exists('references') else []
    if ref_files:
        file_card_selector(ref_files, 'references', 'selected_ref')
    else:
        st.info("업로드된 관련자료가 없습니다.")
