import streamlit as st
import os
import openai
from PIL import Image

from utils import *

icon = Image.open(os.path.dirname(__file__) + '/../icon.png')

st.set_page_config(page_icon=icon)

st.markdown('# 🤖 Prompt Engine')

st.write("Prompt engineering is about giving correct instructions to GPT-4. The more precise the instructions, the better the results. The goal is to generate Manim code from a specific part of code. Than you can use the code to render the animation.")

st.write("## Hello! The new demo it's on [GM Demo](https://generative-manim.vercel.app) :rocket:")
