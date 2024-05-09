# Generative Manim Datasets

Some of the techniques to create better prompt-to-code Manim models will need a guide for training. In order to achieve that we need to compile a dataset of prompts and the corresponding code.

## Sources

### Manim (Community)

- [Examples Gallery](https://docs.manim.community/en/stable/examples.html)

### Manim

- [Quickstart](https://3b1b.github.io/manim/getting_started/quickstart.html)
- [Example Scenes](https://3b1b.github.io/manim/getting_started/example_scenes.html#graphexample)

## Datasets

Now, the structure we need to follow is to create a dataset with the following columns:
- `prompt`: Prompt to generate the code.
- `code`: Corresponding code.
- `type`: Type of media (`video`, `image`).

Altough we are focused on video generation, we should also consider images as a type of media, in order to train the model with vast examples that can be used in different scenarios.

- [*] Extract code examples from the Manim community.
- [ ] Tag each code example with the corresponding type of media (if it uses `self.add`, it is an image, if it uses `self.play`, it is a video).
- [ ] Write a prompt for each code example.
