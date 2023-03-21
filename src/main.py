import streamlit as st
import openai
from manim import *
import re
import os

st.title("Gemanim - Generative Manim")
st.write("Create 2D/3D animations with GPT-3.5 or experiment with GPT-4. :sparkles:")

st.write("This is a two-step process. You first will generate code, then you will able to edit it and render it.")

# "st.session_state object:", st.session_state

# logger.info('initializing session state')

if 'is_code_generated' not in st.session_state:
  st.session_state['is_code_generated'] = False
  st.session_state['code_input'] = ""

prompt = st.text_area("Write your animation idea here", "Draw a blue circle")
openai_api_key = st.text_input(
    "Write your OpenAI API Key", value="", type="password")


def extract_code(text: str) -> str:
  pattern = re.compile(r"```(.*?)```", re.DOTALL)
  match = pattern.search(text)
  if match:
    return match.group(1).strip()
  else:
    return text


def extract_construct_code(code_str):
  pattern = r"def construct\(self\):([\s\S]*)"
  match = re.search(pattern, code_str)
  if match:
    return match.group(1)
  else:
    return ""

def remove_indentation(text: str) -> str:
  lines = text.split("\n")
  stripped_lines = [line.lstrip() for line in lines]
  return "\n".join(stripped_lines)


generates_code = st.button(
    ":computer: Animate :magic:", type="secondary")

code_response = ""

if generates_code:

  openai.api_key = openai_api_key

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "You only write Manim scripts for animations in Python. Generate code, not text. Do not explain code. Do not add comments. Do not use other library than Manim. At the end use 'self.play' ```from manim import *\n\nclass GeneratedScene(Scene):```\n  def construct(self):\n  # Write here"},
                {"role": "user", "content": f"Animation Request: {prompt}. Only code."}],
      max_tokens=200
  )

  code_response = extract_code(response.choices[0].message.content)

  logger.info(response.choices[0].message.content)

  generates_rendering = st.button("Render above code", type="primary")

  logger.info(code_response)
  code_response = remove_indentation(extract_construct_code(code_response))
  st.session_state['is_code_generated'] = True

  # if os.path.exists("media/videos/1080p60.0/GeneratedScene.mp4"):
  #   os.remove("media/videos/1080p60.0/GeneratedScene.mp4")

# if st.session_state['is_code_generated']:
  st.text_area(label="Code generated: ",
               value=code_response,
               key="code_input")

  class GeneratedScene(Scene):
    def construct(self):
      exec(code_response)

  GeneratedScene().render()
  st.video("media/videos/1080p60.0/GeneratedScene.mp4")

# render_animation = st.button(
#     "Render animation :magic_wand:", type="primary")

# if render_animation:
