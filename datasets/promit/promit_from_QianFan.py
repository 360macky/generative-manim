"""
This file is designed to invoke Wenxinyi GPT under Baidu QianFan integration 
to generate possible prompt words for specifying manim code.
---
To use it, add the corresponding Key in API_key.cfg'''QIANFAN_AK/QIANFAN_SK'''

External file:./API_Key.cfg
Depends:pip install qianfan>=0.3.11
"""

import os
import configparser
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.language_models.chat_models import HumanMessage
from langchain_core.prompts import ChatPromptTemplate

ABS_PATH = os.path.dirname(os.path.abspath(__file__))

assert os.path.exists(
    f"{ABS_PATH}/API_Key.cfg"
), f"can not find the {ABS_PATH}/API_Key.cfg"

# Load Setttings
CFG_API_KEY = configparser.ConfigParser()
CFG_API_KEY.read(f"{ABS_PATH}/API_Key.cfg", encoding="utf-8")

os.environ["QIANFAN_AK"] = str(CFG_API_KEY["qianfan"]["QIANFAN_AK"])
os.environ["QIANFAN_SK"] = str(CFG_API_KEY["qianfan"]["QIANFAN_SK"])
print(os.environ["QIANFAN_AK"], os.environ["QIANFAN_SK"])

# Chat stream, integrated with LangChain
chat_QianFan = QianfanChatEndpoint(
    streaming=False,
    model="ERNIE-3.5-8K",  # Well, this one is free
)

# input and output
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "If you are a user who is going to use GPT to generate manim code, write the prompt words used by the role according to the code I gave you, write in the same paragraph, do not need to step by step analysis, do not explain your output in the first paragraph:",
        ),
        ("user", "{input}"),
    ]
)
chain = prompt | chat_QianFan
reply = chain.invoke(
    {
        "input": "from manim import * class MyScene(Scene): def construct(self): circle = Circle(radius=2, color=BLUE) self.add(circle)"
    }
)
print(reply.content)
"""
e.g output
Generate the Manim code for me that creates a scene with a blue circle of radius 2 centered at the origin. The circle should appear gradually on the screen from left to right. Include comments in the code to explain each step.
"""

