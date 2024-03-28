import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from subprocess import run, PIPE, Popen, CalledProcessError
import threading

load_dotenv()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "GM API"


@app.route("/text-to-code", methods=["POST"])
def text_to_code():
    # TODO: To be implemented
    return jsonify({"message": "Not implemented yet"}), 501


@app.route("/code-to-video", methods=["POST"])
def code_to_video():
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

    # Define a function to run the subprocess in a separate thread
    def run_manim():
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
                print(f"Video URL: {video_storage_file_name}.mp4")
            else:
                print(f"Manim command failed with return code {process.returncode}")
                print(f"stdout: {stdout.decode()}")
                print(f"stderr: {stderr.decode()}")

        except CalledProcessError as e:
            print(f"Subprocess error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    # Start the subprocess in a new thread
    threading.Thread(target=run_manim).start()

    # Immediately respond to the client
    # This is the confirmation of reception...
    return jsonify({"message": "Video generation in progress"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
