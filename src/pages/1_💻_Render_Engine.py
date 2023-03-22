import streamlit as st
from manim import *

st.title('💻 Render Engine')

st.write("Quick engine to render Manim code. Paste your code, and click generate. That's it!")

code_response = st.text_area(label="Code generated: ",
                             value="",
                             key="code_input")

generates_code = st.button(
    ":computer: Render video :sparkles:", type="primary")

if generates_code:
  class GenScene(Scene):
    def construct(self):
      exec(code_response)

  GenScene().render()
  try:
    st.video("media/videos/1080p60.0/GenScene.mp4")
  except FileNotFoundError:
    st.error("Error: I couldn't find the generated video file. I know this is a bug and I'm working on it. Please reload the page.")
  except:
    st.error("Error: Something went wrong processing your prompt. Please reload the page.")
