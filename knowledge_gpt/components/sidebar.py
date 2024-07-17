import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Upload a  in pdf, docx, or txt format\n"
            "2. Ask a question about the document💬\n"
        )

        st.session_state["OPENAI_API_KEY"] = st.secrets.openai_api_key

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "BLS Assistant allows you to ask questions about studies "
            "and get accurate answers with instant citations. "
            "At the moment only one document is supoprted at a time. "
            "We are working on adding support for multiple documents. "
        )
        st.markdown(
            "This tool is a work in progress... "
        )
        st.markdown("---")

        # faq()
