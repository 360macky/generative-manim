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

code_example = """circle = Circle(color=BLUE)
self.play(Create(circle))
square = Square(color=RED)
self.play(Transform(circle, square))
self.wait()
"""

def add_indentation(string):
  indented_string = ""
  for line in string.splitlines():
    indented_string += " " * 4 + line + "\n"
  return indented_string

code_response = st.text_area(label="Code generated: ",
                             value=code_example,
                             key="code_input")

generates_code = st.button(
    ":computer: Render video :sparkles:", type="primary")

def get_binary_file_downloader_html(bin_file, file_label='File'):
  with open(bin_file, 'rb') as f:
    data = f.read()
  bin_str = base64.b64encode(data).decode()
  href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
  return href

if generates_code:

  if os.path.exists(os.path.dirname(__file__) + '/../../GenScene.py'):
    os.remove(os.path.dirname(__file__) + '/../../GenScene.py')
  
  if os.path.exists(os.path.dirname(__file__) + '/../../GenScene.mp4'):
    os.remove(os.path.dirname(__file__) + '/../../GenScene.mp4')

  code_response = add_indentation(code_response)
  code_file = create_file_content(code_response)

  with open("GenScene.py", "w") as f:
    f.write(code_file)

  os.system("manim GenScene.py GenScene --format=mp4 --media_dir . --custom_folders video_dir")

  video_file = open(os.path.dirname(__file__) + '/../../GenScene.mp4', 'rb')
  video_bytes = video_file.read()
  st.video(video_bytes)
  python_file = open(os.path.dirname(__file__) + '/../../GenScene.py', 'rb')
  st.download_button("Download scene in Python", python_file, "GenScene.py", "text/plain")
