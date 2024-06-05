# -*- coding: utf-8 -*-
"""Generative Manim Claude Sonnet

Support for code generation in Manim with Claude Sonnet
"""

import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

user_prompt = input("Input the prompt to generate code: ")

# TODO: Sytem prompt to be enhanced
CLAUDE_SYSTEM_INSTRUCTIONS = """Write Manim scripts for animations in Python. Generate code, not text. Never explain code. Never add functions. Never add comments. Never infinte loops. Never use other library than Manim/math. Only complete the code block. Use variables with length of maximum 2 characters. At the end use 'self.play'.

```
from manim import *
from math import *

class GenScene(Scene):
    def construct(self):
        # Write here
```"""

message = client.messages.create(
    max_tokens=1024,
    system=CLAUDE_SYSTEM_INSTRUCTIONS,
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
    model="claude-3-sonnet-20240229",
)
print(message.content)
