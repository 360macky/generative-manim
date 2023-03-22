import streamlit as st
import os
from PIL import Image

st.title("⚡️ How it works")

st.write("## Concept")

st.markdown("""

Imagine a future where you can watch an animation video from a concept you have in your mind in a few seconds. That could be useful for teachers, students, and more. You won't need to learn how to use a video editor, how to draw, or how to code. You just need to write a text.

That indeed is a future. But it's not that far. We can already start working on it. I have a feel that a pure AI editor like [Runway](https://runwayml.com), or an animation editor like [Jitter](https://jitter.video) could take advantage of a workflow like this.

Storytelling, teaching, and creating it's about to change.




The idea behind *Generative Manim* is test how far we can go with GPT-3.5 and GPT-4.

In 2020, (Shreenabh Agrawal)[https://twitter.com/ShreenabhA] did the same with the previous GPT-3.

And there are other users that did the same with that model.

But now, with GPT-3.5, we can do more.


""")

st.write(os.path.dirname(__file__) + "/blueprint.png")
            
blueprint = Image.open(os.path.dirname(__file__) + "/blueprint.png")

st.image(blueprint, caption="Blueprint of Generative Manim", output_format="PNG")

st.write("## Acknowledgements")

st.markdown("""

- [Ashish Shukla](https://github.com/treuille/streamlit-manim/issues/1#issuecomment-1475134874) - For providing the Docker to run Manim in Streamlit.
- [Manim Reddit Community](https://www.reddit.com/r/manim/) - The community of Manim developers.
- [OpenAI Community](https://community.openai.com) - The community of OpenAI developers.
- [Machine Learning Street Talk](https://twitter.com/MLStreetTalk/status/1636647985621745664) - The other tweet that inspired this concept for the GPT-4 application.

""")
