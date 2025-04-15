import streamlit as st
from rag_pipeline import qa_chain
import fitz  # PyMuPDF
import re

st.set_page_config(page_title="Patient Lab Report Explainer", layout="centered")

st.title("🧬 Patient Lab Report Explainer")

st.markdown("Upload a PDF of your lab report or enter the details manually.")

# --- Upload PDF ---
uploaded_file = st.file_uploader("📄 Upload Lab Report (PDF)", type="pdf")

def extract_lab_data_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    # Simple pattern to match things like: "Hemoglobin: 13.5 g/dL"
    lab_pattern = re.findall(r"([A-Za-z\s]+):\s*([\d.]+)\s*([a-zA-Z/%μ]*)", text)
    lab_data = [
        f"{name.strip()}: {value.strip()} {unit.strip()}"
        for name, value, unit in lab_pattern
    ]
    return lab_data, text

if uploaded_file:
    st.info("✅ PDF uploaded. Extracting lab data...")
    lab_data, full_text = extract_lab_data_from_pdf(uploaded_file)

    if lab_data:
        st.success("✅ Extracted Lab Data:")
        for item in lab_data:
            st.write(f"- {item}")
    else:
        st.warning("⚠️ Couldn't detect lab values. Please enter manually.")

    # Auto-generate a question from lab data
    combined_question = "Explain the following lab results in simple terms:\n" + "\n".join(lab_data)
    query = st.text_area("📝 Modify your question (optional)", combined_question)
else:
    query = st.text_input("🩺 Enter your question (e.g., 'What does a high creatinine mean?')")

if st.button("Generate Explanation") and query:
    with st.spinner("Generating explanation..."):
        result = qa_chain.run(query)
        st.subheader("📘 Explanation")
        st.write(result)
