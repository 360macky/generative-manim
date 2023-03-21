import streamlit as st
from manim import *
import openai
import re

st.title(":art: Generative Manim")
st.write(":robot_face: Create quick animations with GPT-3.5. :sparkles:")

if 'is_code_generated' not in st.session_state:
  st.session_state['is_code_generated'] = False
  st.session_state['code_input'] = ""

prompt = st.text_area("Write your animation idea here. Use simple words.", "Draw a blue circle and convert it to a red square")

if st.checkbox("Use my own [Open API Key](https://platform.openai.com/account/api-keys)"):
  openai_api_key = st.text_input("Paste your own [Open API Key](https://platform.openai.com/account/api-keys)", value="", type="password")

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

  if not openai_api_key:
    # get the default API key from secrets
    openai.api_key = st.secrets["openai_api_key"]
  else:
    openai.api_key = openai_api_key

  # If prompt exceeds 240 characters, it will be truncated
  if len(prompt) > 240:
    st.error("Error: Your prompt is longer than 240 characters. Please shorten it, or use your own API key.")
    st.stop()

  

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "You write Manim scripts for animations in Python. Generate code, not text. Do not explain code. Do not add comments. Do not use other library than Manim. At the end use 'self.play' ```from manim import *\n\nclass GenScene(Scene):```\n  def construct(self):\n  # Write here"},
                {"role": "user", "content": f"New Animation Request: {prompt}"}],
      max_tokens=300
  )

  code_response = extract_code(response.choices[0].message.content)

  code_response = remove_indentation(extract_construct_code(code_response))
  st.session_state['is_code_generated'] = True

  if show_code:
    st.text_area(label="Code generated: ",
                 value=code_response,
                 key="code_input")

  class GenScene(Scene):
    def construct(self):
      exec(code_response)

  GenScene().render()
  st.video("media/videos/1080p60.0/GenScene.mp4")

st.write('Made with :heart: by [Marcelo Arias](https://github.com/360macky).')
st.write('[Source code](https://github.com/360macky/generative-manim) - [Report a bug](https://github.com/360macky/generative-manim/issues/new) - [Twitter](https://twitter.com/360macky)')
