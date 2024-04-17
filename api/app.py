import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from subprocess import run, PIPE, Popen, CalledProcessError
import threading
from openai import OpenAI

load_dotenv()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "GM API"


@app.route("/zero-shot-learning", methods=["POST"])
def zero_shot_learning():
    text = request.json.get("text")
    prompt = f"Generate python code for the following text:\n\n{text}"
    client = OpenAI()
    GPT_SYSTEM_INSTRUCTIONS = """Write Manim scripts for animations in Python. Generate code, not text. Never explain code. Never add functions. Never add comments. Never infinte loops. Never use other library than Manim/math. Only complete the code block. Use variables with length of maximum 2 characters. At the end use 'self.play'.

```
from manim import *
from math import *

class GenScene(Scene):
    def construct(self):
        # Write here
```"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": GPT_SYSTEM_INSTRUCTIONS},
            {"role": "user", "content": prompt},
        ],
    )
    
    code = response.choices[0].message
    return jsonify({"code": code}), 200


@app.route("/code-to-video", methods=["POST"])
def code_to_video():
    print("Request received")

    # Get the code and file_name from the POST request
    code = request.json.get("code")
    file_name = request.json.get("file_name")
    file_class = request.json.get("file_class")
    iteration = request.json.get("iteration")
    video_storage_file_name = f"video-{iteration}"

    if not code:
        return jsonify(error="No code provided"), 400

    # Write the code to a file with the specified file_name
    with open(file_name, "w") as f:
        f.write(code)

    try:
        process = Popen(
            [
                "manim",
                file_name,
                file_class,
                "--format=mp4",
                "--media_dir",
                ".",
                "--custom_folders",
            ],
            stdout=PIPE,
            stderr=PIPE,
            cwd=os.path.dirname(os.path.realpath(__file__)),
        )

        # Wait for the subprocess to finish and capture stdout and stderr
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            print("Video created")
            return jsonify({"message": "Video generation completed"})
        else:
            print(f"Manim command failed with return code {process.returncode}")
            print(f"stdout: {stdout.decode()}")
            print(f"stderr: {stderr.decode()}")
            return (
                jsonify({"error": f"Video generation failed: {stderr.decode()}"}),
                500,
            )
    except CalledProcessError as e:
        print(f"Subprocess error: {e}")
        return jsonify({"error": f"Subprocess error occurred: {e}"}), 500
    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": f"Unexpected error occurred: {e}"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
