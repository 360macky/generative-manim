# Generative Manim Datasets

Some of the techniques to create better prompt-to-code Manim models will need a guide for training. In order to achieve that we need to compile a dataset of prompts and the corresponding code.

## Sources

### Manim (Community)

- [Examples Gallery](https://docs.manim.community/en/stable/examples.html)

### Manim

- [Quickstart](https://3b1b.github.io/manim/getting_started/quickstart.html)
- [Example Scenes](https://3b1b.github.io/manim/getting_started/example_scenes.html#graphexample)

## Datasets

### Custom Dataset

Now, the structure we need to follow is to create a dataset with the following columns:
- `prompt`: Prompt to generate the code.
- `code`: Corresponding code.
- `type`: Type of media (`video`, `image`).

Altough we are focused on video generation, we should also consider images as a type of media, in order to train the model with vast examples that can be used in different scenarios.

- [x] Extract code examples from the Manim community.
- [ ] Tag each code example with the corresponding type of media (if it uses `self.add`, it is an image, if it uses `self.play`, it is a video).
- [ ] Write a prompt for each code example.

### Dataset from `Edoh`

Extracting the dataset of prompts and code from the [Edoh Manim Python](https://huggingface.co/datasets/Edoh/manim_python) dataset we got `edoh-dataset.jsonl`.

The dataset contains 599 examples of prompts and code.

```json
{"messages": [{"role": "system", "content": "Write Manim scripts for animations in Python. Generate code, not text."}, {"role": "user", "content": "Create a new scene named 'MyScene'."}, {"role": "assistant", "content": "from manim import * class MyScene(Scene): def construct(self): pass"}]}
{"messages": [{"role": "system", "content": "Write Manim scripts for animations in Python. Generate code, not text."}, {"role": "user", "content": "Add a circle with radius 2 and center at the origin to the scene."}, {"role": "assistant", "content": "from manim import * class MyScene(Scene): def construct(self): circle = Circle(radius=2, color=BLUE) self.add(circle)"}]}
{"messages": [{"role": "system", "content": "Write Manim scripts for animations in Python. Generate code, not text."}, {"role": "user", "content": "Create a text object saying 'Hello, World!' and add it to the scene."}, {"role": "assistant", "content": "from manim import * class MyScene(Scene): def construct(self): text = Text('Hello, World!') self.add(text)"}]}
```
