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
code_input = st.text_area(
    "Write your animation idea here", value=code_response)


def extract_construct_content(source_code):
  pattern = r"def construct\(self\):([\s\S]+?)\n\s*(?=[^ \t])"
  match = re.search(pattern, source_code)
  if match:
    return match.group(1)
  else:
    return None


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

  code_response = extract_construct_content(
      response.choices[0].message.content)

  if code_response is None:
    logger.error("We could not extract the code from the response.")
    logger.info(f"Response: {response.choices[0].message.content}")
  else:
    logger.info(f"Awesome. Code response: {code_response}")

  if generates_animation:
    class GeneratedScene(Scene):
      def construct(self):
        exec(code_response)
    GeneratedScene().render()
    st.video("media/videos/1080p60.0/GeneratedScene.mp4")
