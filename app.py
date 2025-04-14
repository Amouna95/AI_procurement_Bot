import streamlit as st
import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="AI Procurement Bot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
            padding: 2rem;
            border-radius: 15px;
        }
        .title {
            font-size: 3rem;
            font-weight: 800;
            color: #1f4e79;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.3rem;
            font-weight: 400;
            color: #333333;
            text-align: center;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Interface principale
with st.container():
    st.markdown('<div class="title">🤖 AI Procurement Bot</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Powered by the Advanced RAG App – Handle PDFs, Web pages, Videos, Audios & Texts</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🚀 Navigation")

    # Navigation vers les autres pages
    pg = st.navigation([
        st.Page("add_documents.py", title="📄 Add Document", icon="1️⃣"),
        st.Page("chatbot.py", title="💬 Chat with Documents", icon="2️⃣")
    ])
    pg.run()
