import streamlit as st

st.set_page_config(
    page_title="AI Procurement Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Procurement Assistant")

st.write(
    "Upload an RFQ document and let AI analyze it."
)

uploaded_file = st.file_uploader(
    "Upload RFQ PDF",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Analyze RFQ"):
        st.info("AI analysis will be added in the next step.")