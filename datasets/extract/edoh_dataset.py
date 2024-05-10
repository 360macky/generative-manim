import json
from datetime import datetime
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("Edoh/manim_python")

# Prepare the output file name with a timestamp
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
output_file = f"edoh-dataset-{timestamp}.jsonl"

# Open the file for writing
with open(output_file, 'w') as f:
    # Iterate over each example in the dataset
    for example in dataset['train']:
        # Create the structured message
        entry = {
            "messages": [
                {"role": "system", "content": "Write Manim scripts for animations in Python. Generate code, not text."},
                {"role": "user", "content": example['instruction']},
                {"role": "assistant", "content": example['output']}
            ]
        }
        # Write the JSON entry to the file
        f.write(json.dumps(entry) + '\n')

print(f"Dataset converted and saved to {output_file}")
