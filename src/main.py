import streamlit as st
import openai
from manim import *
import re

st.title("Gemanim - Generative Manim")
st.write("Create 2D/3D animations with GPT-3.5 or experiment with GPT-4. :sparkles:")

code_response = '''
circle = Circle()
circle.set_fill("#FF0000", opacity=0.5)
self.play(Create(circle))
'''

prompt = st.text_area("Write your animation idea here", "Draw a blue circle")
openai_api_key = st.text_input(
    "Write your OpenAI API Key", value="", type="password")
# code_input = st.text_area(
#  "Write your animation idea here", value=code_response)

def extract_code(text: str) -> str:
  pattern = re.compile(r"```(.*?)```", re.DOTALL)
  match = pattern.search(text)

  if match:
    return match.group(1).strip()
  else:
    return ""

def extract_construct_content(code: str) -> str:
  pattern = re.compile(r"def construct\(self\):(\n\s*(?:.*))+")
  match = pattern.search(code)

  if match:
    body = match.group(0)
    body = re.sub(r"def construct\(self\):", "", body)
    return body.strip()
  else:
    return ""

def remove_indentation(text):
  lines = text.split("\n")
  stripped_lines = [line.lstrip() for line in lines]
  return "\n".join(stripped_lines)


generates_only_code = st.button(
    "Generate only code :computer:", type="secondary")
generates_animation = st.button(
    "Generate animation :magic_wand:", type="primary")

if generates_animation or generates_only_code:

  openai.api_key = openai_api_key

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "system", "content": "You only write Manim scripts for animations in Python. Generate code, not text. Do not explain code. Do not use other library than Manim. At the end use 'self.play' ```from manim import *\n\nclass GeneratedScene(Scene):```\n  def construct(self):\n  # Write here"},
                {"role": "user", "content": f"Animation Request: {prompt}. Only code."}],
      max_tokens=200
  )

  code_response = extract_code(response.choices[0].message.content)

  logger.info(response.choices[0].message.content)

  generates_rendering = st.button("Render above code", type="primary")

  if code_response is None:
    logger.error("We could not extract the code from the response.")
    logger.info(f"Response: {response.choices[0].message.content}")
  else:
    logger.info(f"Awesome. Code response: {code_response}")
    code_response = remove_indentation(code_response)
    code_response = st.text_area(label="Code generated: ", value=code_response)

  if generates_animation or generates_rendering:
    class GeneratedScene(Scene):
      def construct(self):
        exec(code_response)
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")
