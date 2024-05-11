"""
This file is designed to invoke OpenAI GPT-4
to generate possible prompt words for specifying manim code.
"""

import os
import openai
from openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Define the GPT-4 model endpoint
llm = ChatOpenAI(model="gpt-4", openai_api_key=os.environ["OPENAI_API_KEY"])

# input and output
chain = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "If you are a user who is going to use GPT to generate manim code, write the prompt words used by the role according to the code I gave you, write in the same paragraph, do not need to step by step analysis, do not explain your output in the first paragraph:",
        ),
        (
            "user",
            "{input}",
        ),
    ]
)

reply = chain.format_messages(
    input="from manim import * class MyScene(Scene): def construct(self): circle = Circle(radius=2, color=BLUE) self.add(circle)"
)

print(llm(reply).content)
"""
e.g output
Generate the Manim code for me that creates a scene with a blue circle of radius 2 centered at the origin. The circle should appear gradually on the screen from left to right. Include comments in the code to explain each step.
"""
