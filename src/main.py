import streamlit as st
from manim import *
import openai
import re

st.title("Generative Manim")
st.write(":robot_face: Create quick animations with GPT-3.5. :sparkles:")

if 'is_code_generated' not in st.session_state:
  st.session_state['is_code_generated'] = False
  st.session_state['code_input'] = ""

prompt = st.text_area("Write your animation idea here", "Draw a blue circle and convert it to a red square")
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


generates_code = st.button(":computer: Animate :sparkles:", type="primary")
show_code = st.checkbox("Show generated code")

code_response = ""

if generates_code:

  openai.api_key = openai_api_key

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "You only write Manim scripts for animations in Python. Generate code, not text. Do not explain code. Do not add comments. Do not use other library than Manim. At the end use 'self.play' ```from manim import *\n\nclass GeneratedScene(Scene):```\n  def construct(self):\n  # Write here"},
                {"role": "user", "content": f"New Animation Request: {prompt}. Only code."}],
      max_tokens=300
  )

  code_response = extract_code(response.choices[0].message.content)

  code_response = remove_indentation(extract_construct_code(code_response))
  st.session_state['is_code_generated'] = True

  if show_code:
    st.text_area(label="Code generated: ",
                 value=code_response,
                 key="code_input")

  class GeneratedScene(Scene):
    def construct(self):
      exec(code_response)

  GeneratedScene().render()
  st.video("media/videos/1080p60.0/GeneratedScene.mp4")

st.write('Made with :heart: by [Marcelo Arias](https://github.com/360macky).')
