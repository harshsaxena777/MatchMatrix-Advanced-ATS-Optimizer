import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Harsh M. | AI Portfolio", page_icon="🚀", layout="wide")

# --- CUSTOM FANCY CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0f172a;
    }
    
    .main {
        background: radial-gradient(circle at top right, #1e293b, #0f172a);
    }

    /* Glassmorphism Card Style */
    .project-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        transition: all 0.3s ease;
        margin-bottom: 20px;
        height: 280px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border-color: #38bdf8;
        box-shadow: 0 10px 30px -10px rgba(56, 189, 248, 0.3);
    }

    .tag {
        background: #0ea5e9;
        color: white;
        padding: 2px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: bold;
        margin-right: 5px;
    }

    .btn-launch {
        background-color: #38bdf8;
        color: white !important;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        display: block;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🚀 Engineering Portfolio Hub")
st.markdown("#### B.Tech AI & Data Science Specialization")
st.write("Welcome to my technical dashboard. Below are four production-ready AI/ML applications demonstrating full-stack engineering capabilities.")

st.markdown("---")

# --- PROJECT GRID ---
def create_card(title, description, tags, link):
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in tags])
    st.markdown(f"""
        <div class="project-card">
            <div>
                <h3 style="color:#38bdf8; margin-bottom:10px;">{title}</h3>
                <p style="color:#94a3b8; font-size:0.9rem;">{description}</p>
                <div style="margin-top:10px;">{tags_html}</div>
            </div>
            <a href="{link}" target="_blank" class="btn-launch">Launch Application →</a>
        </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    create_card(
        "NexaLap AI", 
        "A machine learning engine predicting laptop prices based on hardware configurations using Random Forest Regressor.",
        ["ML", "Scikit-Learn", "Regression"],
        "https://nexalap.streamlit.app"
    )
    create_card(
        "VoxBrief NLP", 
        "Generative AI tool that leverages HuggingFace Transformers to provide neural summaries of long documents.",
        ["NLP", "Transformers", "GenAI"],
        "https://voxbrief.streamlit.app"
    )

with col2:
    create_card(
        "QuantPulse Terminal", 
        "Real-time technical analysis dashboard fetching live data via Yahoo Finance API with Plotly Candlestick charts.",
        ["API", "Finance", "DataViz"],
        "https://quantpulse.streamlit.app"
    )
    create_card(
        "MatchMatrix ATS", 
        "Computational linguistics tool using TF-IDF and Cosine Similarity to score resume alignment against job descriptions.",
        ["Text Analytics", "Linguistics", "PDF"],
        "https://matchmatrix.streamlit.app"
    )

# --- TECH STACK SECTION ---
st.markdown("---")
st.subheader("🛠 Technical Expertise")
cols = st.columns(4)
with cols[0]: st.info("**Languages:** Python, C++, SQL")
with cols[1]: st.info("**AI/ML:** TensorFlow, PyTorch, Sklearn")
with cols[2]: st.info("**Data:** Pandas, NumPy, Plotly")
with cols[3]: st.info("**Cloud:** AWS, GitHub Actions, Streamlit")