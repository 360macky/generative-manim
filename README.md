<p align="center">
  <img
    src=".github/logo.png"
    align="center"
    width="100"
    alt="Generative Manim"
    title="Generative Manim"
  />
  <h1 align="center">Generative Manim</h1>
</p>

<p align="center">
  🎨 GPT-4 powered generative videos. Concept. ⚡️ <a href="https://discord.gg/FG8BAcdE">Join our Discord server here!</a>
</p>

<p align="center">
  <a href="https://generative-manim.streamlit.app">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" />
  </a>
  <a href="">
    <img src="https://img.shields.io/static/v1?label=OpenAI%20API&message=GPT-4&color=000000&logo=openai&style=flat" />
  </a>
</p>

---

![Preview](./.github/preview.jpg)

## 🚀 Concept

**Generative Manim** (GM) is a suite of tools that allows you to create videos with Manim using LLMs (Large Language Models) like GPT-4. The idea is to make the process of creating videos more accessible to everyone.

It began as a prototype of a web app that uses [GPT-4](https://openai.com/research/gpt-4) to generate videos with [Manim](https://www.manim.community). The idea behind this project is taking advantage of the power of GPT-4 in programming, the understanding of human language and the animation capabilities of Manim to generate a tool that could be used by anyone to create videos. Regardless of their programming or video editing skills.

## 🎒 Streamlit

Integration of the GM with Streamlit. Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create interactive web apps for your projects with minimal effort.

### 🛠 Core Development

Generative Manim is built with [Streamlit](https://streamlit.io). It uses [OpenAI API](https://platform.openai.com/docs/api-reference/introduction) to make requests to GPT-4 and GPT-3.5-turbo.

![Blueprint](./src/pages/blueprint.png)

For more details, check out the [How it works](https://generative-manim.streamlit.app/%EF%B8%8F_How_it_works) section.

## 🤖 Chatbot Platform

🏗️ Integration as a chatbot in progress.

## 💬 REST API

In `/api/app.py` you can find the REST API. Currently the available endpoint is `/zero-shot-learning`, which is the legacy basic system-prompt concept of the project.

## 🦜 LangChain

🏗️ Integration with **LangChain** in progress.

#### 📦 Installation

Once you have cloned the repository, you need to install streamlit and set `OPENAI_API_KEY` as an environment variable in your system.

To start the app, run:

```
streamlit run src/main.py
```

## 🤲 Contributing

Generative Manim is an open source project.

If you want to be the author of a new feature, fix a bug or contribute with something new.

Fork the repository and make changes as you like. [Pull requests](https://github.com/360macky/generative-manim/pulls) are warmly welcome. Remember you can also join our [Discord server](https://discord.gg/FG8BAcdE) to discuss new features, bugs or any other topic.
