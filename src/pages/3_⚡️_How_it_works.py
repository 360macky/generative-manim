import streamlit as st
import os
from PIL import Image

st.title("⚡️ How it works")

st.write("## Concept")

st.markdown("""

Imagine a future where you can watch an animation video from a concept you have in your mind in a few seconds. That could be useful for teachers, students, and more. You won't need to learn how to use a video editor, how to draw, or how to code. You just need to write a descriptive text.

That indeed is a future. But it's not that far. We can already start working on it. I have a feel that a pure AI editor like [Runway](https://runwayml.com), or an animation editor like [Jitter](https://jitter.video) could take advantage of a workflow like this:

""")

blueprint = Image.open(os.path.dirname(__file__) + "/blueprint.png")

st.image(blueprint, caption="Blueprint of Generative Manim", output_format="PNG")

st.markdown("""

Storytelling, teaching, and creating it's about to change with this.

The idea behind *Generative Manim* is test how far we can go with GPT-3.5 and GPT-4.

## Costs implications

Currently GPT-4 is 30 times more expensive than GPT-3.5. That means that a 1000 tokens text will cost $30. That's a lot of money. But it's not that much if you think about the possibilities.

""")


st.write("## Acknowledgements")

st.markdown("""

- [Ashish Shukla](https://github.com/treuille/streamlit-manim/issues/1#issuecomment-1475134874) - For providing the Docker to run Manim in Streamlit.
- [Manim Reddit Community](https://www.reddit.com/r/manim/) - The community of Manim developers.
- [OpenAI Community](https://community.openai.com) - The community of OpenAI developers.
- [Machine Learning Street Talk](https://twitter.com/MLStreetTalk/status/1636647985621745664) - The other tweet that inspired this concept for the GPT-4 application.

""")
