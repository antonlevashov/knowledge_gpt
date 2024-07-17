import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload a pdf, docx, or txt file📄\n"
            "2. Ask a question about the document💬\n"
        )

        st.session_state["OPENAI_API_KEY"] = st.secrets.openai_api_key

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "BLS Assistant allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
        )
        st.markdown("---")

        # faq()
