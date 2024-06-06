import streamlit as st
from manim import *
import os
import base64
from PIL import Image

from utils import *

icon = Image.open(os.path.dirname(__file__) + '/../icon.png')

st.set_page_config(page_icon=icon)

styl = f"""
<style>
  textarea {{
    font-family: 'Consolas', monospace !important;
  }}
  }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)

st.title('💻 Render Engine')

st.write("Quick engine to render Manim code. Paste your code, and click generate. That's it!")

st.write("## Hello! The new demo it's on [GM Demo](https://generative-manim.vercel.app) :rocket:")
