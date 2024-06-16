"""
GM (Generative Manim) API is licensed under the Apache License, Version 2.0
"""

import os
import time
from subprocess import run, PIPE, Popen, CalledProcessError
import subprocess
import urllib.parse
import requests
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import threading
from openai import OpenAI
import anthropic

load_dotenv()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Generative Manim API"


@app.route("/generate-code", methods=["POST"])
def generate_code():
    body = request.json
    prompt_content = body.get("prompt", "")
    model = body.get("model", "gpt-4o")

    general_system_prompt = """
You are an assistant that knows about Manim. Manim is a mathematical animation engine that is used to create videos programmatically.

The following is an example of the code:
\`\`\`
from manim import *
from math import *

class GenScene(Scene):
def construct(self):
    c = Circle(color=BLUE)
    self.play(Create(c))

\`\`\`

# Rules
1. Always use GenScene as the class name, otherwise, the code will not work.
2. Always use self.play() to play the animation, otherwise, the code will not work.
3. Do not use text to explain the code, only the code.
4. Do not explain the code, only the code.
    """

    if model.startswith("claude-"):
        client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        messages = [{"role": "user", "content": prompt_content}]
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                temperature=0.2,
                system=general_system_prompt,
                messages=messages,
            )

            # Extract the text content from the response
            code = "".join(block.text for block in response.content)

            return jsonify({"code": code})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    else:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        messages = [
            {"role": "system", "content": general_system_prompt},
            {"role": "user", "content": prompt_content},
        ]

        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.2,
            )

            code = response.choices[0].message.content

            return jsonify({"code": code})

        except Exception as e:
            return jsonify({"error": str(e)}), 500


def upload_to_azure_storage(file_path, video_storage_file_name):
    cloud_file_name = f"{video_storage_file_name}.mp4"

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=cloud_file_name
    )

    # Upload the video file
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    # Construct the URL of the uploaded blob
    blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{cloud_file_name}"
    return blob_url


@app.route("/code-to-video", methods=["POST"])
def code_to_video():
    print("Request received")

    # Get the code and file_name from the POST request
    code = request.json.get("code")
    file_name = request.json.get("file_name")
    file_class = request.json.get("file_class")
    iteration = request.json.get("iteration")
    aspect_ratio = request.json.get("aspect_ratio")

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
            video_file_path = os.path.join("GenScene.mp4")
            video_url = upload_to_azure_storage(
                video_file_path, video_storage_file_name
            )
            return jsonify(
                {"message": "Video generation completed", "video_url": video_url}
            )
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
    app.run(debug=False, host="0.0.0.0", port=port)
