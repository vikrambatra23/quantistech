import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Quantis Tech",
    page_icon="🔷",
    layout="wide"
)

st.markdown("""
<style>
#MainMenu, header, footer, .stDeployButton { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=6000, scrolling=True)
