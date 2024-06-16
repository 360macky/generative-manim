# 🔬 Generative Manim API (Animation Processing Interface)

The Animation Processing Interface or API is a REST API that can be used to generate Manim scripts using LLMs and render videos from Python code. This is the API used on [Generative Manim Demo](https://generative-manim.vercel.app/) under the hood.

## 🚀 Concept

We are creating the software that enables you to transform ideas, concepts, and more into animated videos.

Generative Manim API (Animation Processing Interface) empowers you to generate Manim scripts using LLMs and render videos from Python code. This allows seamless integration into your website, app, or any kind of project that requires animations. Happy coding!

## 📦 Installation

### Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/) (optional, if you want to use it)

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/360macky/generative-manim.git
```

2. **Install the requirements:**

```bash
pip install -r requirements.txt
```

2. **Build the Docker image:**

```bash
docker build -t generative-manim-api .

```

3. **Run the Docker container:**

```bash
docker run -p 8080:8080 generative-manim-api
```
