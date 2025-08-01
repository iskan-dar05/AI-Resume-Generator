import streamlit as st

from models.similarity_model import load_similarity_model, encode, calculate_similarity
# from models.tiny_llama_model import load_tiny_llama, generate_cv
from models.llama_model import generate_cv
from utils.pdf_utils import extract_text_from_pdf
from utils.text_utils import clean_text
from utils.pdf_export import save_to_pdf
# from templates.prompts import build_resume_prompt

st.set_page_config(page_title="AI Resume Scanner & Generator", layout="wide")
st.title("📄 AI Resume Scanner & Generator")

# File uploaders
jd_file = st.file_uploader("📥 Upload Job Description (PDF)", type=["pdf"])
cv_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])

# If both uploaded: compare
if jd_file and cv_file:
    st.success("✅ Files uploaded successfully!")

    jd_text = extract_text_from_pdf(jd_file)
    cv_text = extract_text_from_pdf(cv_file)

    clean_jd = clean_text(jd_text)
    clean_cv = clean_text(cv_text)

    st.subheader("🔍 Resume vs Job Description Matching")
    sim_model = load_similarity_model()
    jd_embeds = encode(sim_model, clean_jd)
    cv_embeds = encode(sim_model, clean_cv)

    matches = calculate_similarity(clean_jd, clean_cv, jd_embeds, cv_embeds)

    for m in matches:
        if m["matched"]:
            st.success(f"✅ '{m['jd']}' matched with: '{m['match']}' ({m['score']:.2f})")
        else:
            st.error(f"❌ '{m['jd']}' not found (score: {m['score']:.2f})")

# Llama Resume Generator
if jd_file:
    st.subheader("🧠 Generate Resume with AI (TinyLlama)")

    if st.button("🚀 Generate Resume"):
        jd_text = extract_text_from_pdf(jd_file)

        with st.spinner("Generating resume with TinyLlama..."):
            print(jd_text)
            ai_resume = generate_cv(jd_text)

            st.text_area("📝 Generated Resume", ai_resume, height=500)

            pdf_file = save_to_pdf(ai_resume)
            with open(pdf_file, "rb") as f:
                st.download_button("📄 Download AI Resume", f, file_name="ai_resume.pdf")
