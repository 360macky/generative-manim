import streamlit as st
import os
from PIL import Image

icon = Image.open(os.path.dirname(__file__) + '/../icon.png')

st.set_page_config(page_icon=icon)

st.title("❓ FAQ")

st.markdown("""
If you have any other questions, please tell me at [Twitter](https://twitter.com/360macky)! I'll be happy to answer them.
""")

st.write("## How the future could be?")

st.write("Imagine a video editor that allows you to create animations just by writing a text. Manim could be that way the videos are created.")

st.write("## How can I modify this app?")

st.markdown("""
If you want to experiment over this concept you can fork the [GitHub Repository](https://github.com/360macky/generative-manim), then create an account at [Streamlit](https://streamlit.io/), open the [Dashboard](https://share.streamlit.io/), click on the *New App* button, and then click on the *GitHub* button. Then you can deploy the app to Streamlit, then search for the forked repository, in Main file path write `src/main.py` and finally click on the *Deploy!* button.

Now you can update the cloned repository and view the changes in your Streamlit app. If you believe that your changes are useful, you can open a pull request to the original repository. Pull requests are warmly welcome.
""")

st.write("## What is Manim?")

st.write("Manim is a Python library for creating mathematical animations. It's open source. The version used in this Streamlit app is Manim Community, a fork of the original Manim library.")

st.write("## What is GPT-3.5?")

st.write("GPT-3.5 is the latest stable API-available version of OpenAI's GPT model. It's a language model behind ChatGPT.")

st.write("## What is GPT-4?")

st.write("GPT-4 is the latest (but unstable and limited) version of OpenAI's GPT model. GPT-4 excels at tasks that require advanced reasoning, complex instruction understanding, and more creativity.")

st.write("## What is the purpose of this app?")

st.write("The purpose is to show how GPT-4 and GPT-3.5 can be used to export Manim code from a prompt. The design, which is simple, could be used to empower video editors, or apps in general.")

