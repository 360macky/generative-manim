import os
import subprocess
import streamlit as st
from manim import *
from PIL import Image

from utils import *

icon = Image.open(os.path.dirname(__file__) + '/icon.png')

st.set_page_config(
    page_title="Generative Manim",
    page_icon=icon,
)

styl = f"""
<style>
  textarea[aria-label="Code generated: "] {{
    font-family: 'Consolas', monospace !important;
  }}
  }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)

st.title(":art: Generative Manim")
st.write(":robot_face: Create beautiful and quick animations with GPT-4 and GPT-3.5 :sparkles:")

st.write("## Hello! The new demo it's on [GM Demo](https://generative-manim.vercel.app) :rocket:")

st.write('Made with :heart: by [Marcelo](https://github.com/360macky).')
st.write('[Source code](https://github.com/360macky/generative-manim) - [Report a bug](https://github.com/360macky/generative-manim/issues/new) - [Twitter](https://twitter.com/360macky) - [OpenAI Profile](https://community.openai.com/u/360macky/summary)')
