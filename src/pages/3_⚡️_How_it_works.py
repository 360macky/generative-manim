import streamlit as st
import os
from PIL import Image

icon = Image.open(os.path.dirname(__file__) + '/../icon.png')

st.set_page_config(page_icon=icon)

st.title("⚡️ How it works")

st.markdown("""
**What do you think about Generative Manim so far?**

Please tell me at [Twitter](https://twitter.com/360macky) or open an issue at the [GitHub Repository](https://github.com/360macky/generative-manim).
""")

st.write("## Concept")

st.markdown("""

Imagine a future where you can watch an animation video from a concept you have in your mind in a few seconds. That would be useful for teachers, students, and more. People that want to generate a video won't need to learn how to use a video editor, how to draw, or how to code. You just need to write a descriptive text.

That indeed is a future. And it's not that far. We can already start working on it.

Manim is a Python library for creating complex graphics and animations. The main advantage of Manim for GPT, it's that since it's a language for the LLM, it's more easy to generate proper code from a prompt.

I have a feel that a pure AI editor like [Runway](https://runwayml.com), or an advanced animation editor like [Jitter](https://jitter.video) could take advantage of a workflow like this:

""")

blueprint = Image.open(os.path.dirname(__file__) + "/blueprint.png")

st.image(blueprint, caption="Blueprint of Generative Manim", output_format="PNG")

st.markdown("""

The idea behind *Generative Manim* is test how far we can go with GPT-3.5 and GPT-4.

## Rendering problems

While GPT-3.5 and GPT-4 are able to generate good code. They have the following limitations:

- The information is limited up to 2021. That means Manim features that were added after 2021 won't be available.
- The code generated by GPT-3.5 and GPT-4 is not always correct.

:white_check_mark: At this moment, **Generative Manim** is able to render simple animations that rely on Manim and Math packages.

:x: But it's not able to render really complex animations that could require more lines of code that the limit of tokens provided by GPT-3.5 or GPT-4.

## Costs implications

Currently GPT-4 is 30 times more expensive than GPT-3.5. That means that a 1000 tokens text will cost $30. That's a lot of money. But it's not that much if you think about the possibilities.

I would recommend you to use your own API Key if you want to use this app without character limits.

""")


st.write("## Acknowledgements")

st.markdown("""

- [Ashish Shukla](https://github.com/treuille/streamlit-manim/issues/1#issuecomment-1475134874) - For providing the Docker to run Manim in Streamlit.
- [Manim Reddit Community](https://www.reddit.com/r/manim/) - The community of Manim developers.
- [OpenAI Community](https://community.openai.com) - The community of OpenAI developers.
- [Machine Learning Street Talk](https://twitter.com/MLStreetTalk/status/1636647985621745664) - A tweet that inspired the concept for the GPT-4 application.

""")
