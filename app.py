import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="MatchMatrix ATS", page_icon="🎯")

st.title("🎯 MatchMatrix: ATS Intelligence")
st.markdown("Quantify your resume's alignment with any Job Description using vector similarity.")

jd = st.text_area("Job Description", height=200)
uploaded_file = st.file_uploader("Upload Professional Resume (PDF)", type="pdf")

if uploaded_file and jd:
    reader = PdfReader(uploaded_file)
    resume_text = "".join([page.extract_text() for page in reader.pages])
    
    # Vectorization Logic
    # Math: $$\text{Similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume_text, jd])
    score = cosine_similarity(vectors)[0][1] * 100

    st.header(f"Match Score: {score:.1f}%")
    st.progress(score/100)
    
    if score > 70:
        st.success("Strong Alignment Identified!")
    else:
        st.warning("Needs Optimization for Keywords.")