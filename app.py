import streamlit as st

st.set_page_config(
    page_title="AI PYQ Analyzer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI PYQ Analyzer")

st.write(
    "Analyze previous-year question papers "
    "chapter-wise and identify repeated questions."
)

st.divider()

st.header("📄 Upload Question Papers")

uploaded_files = st.file_uploader(
    "Upload your PYQ PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(
        f"{len(uploaded_files)} question paper(s) uploaded."
    )

    for file in uploaded_files:
        st.write(f"📄 {file.name}")

else:
    st.info("Upload one or more PDF question papers to begin.")