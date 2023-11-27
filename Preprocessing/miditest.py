from miditok import MMM
from miditoolkit import MidiFile
from pathlib import Path

# Creates the tokenizer and list the file paths
tokenizer = MMM()  # using defaults parameters (constants.py)
tokenizer._load_params(Path("tokenizer", "tokenizer.json"))
tokens = tokenizer.load_tokens("../Datasets/jsfakes-tok/bpe/0.json")
print(tokens)
generated_midi = tokenizer(tokens['ids'])  # MidiTok can handle PyTorch / Tensorflow Tensors
generated_midi.dump('file.mid')  # could have been done above by giving the path argument

