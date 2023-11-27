from miditok import MMM
from miditoolkit import MidiFile
from pathlib import Path

# Creates the tokenizer and list the file paths
tokenizer = MMM()  # using defaults parameters (constants.py)
midi_paths = list(Path("../Datasets/jsfakes-midi").glob("**/*.mid"))
data_augmentation_offsets = [2, 1, 1]  # data augmentation on 2 pitch octaves, 1 velocity and 1 duration values
tokenizer.tokenize_midi_dataset(midi_paths, Path("../Datasets/jsfakes-tok/no_bpe"),
                                data_augment_offsets=data_augmentation_offsets)

# Constructs the vocabulary with BPE, from the token files
tokenizer.learn_bpe(
    vocab_size=10000,
    tokens_paths=list(Path("../Datasets/jsfakes-tok/no_bpe").glob("**/*.json")),
    start_from_empty_voc=False,
)

# Saving our tokenizer, to retrieve it back later with the load_params method
tokenizer.save_params(Path("tokenizer", "tokenizer.json"))
# Applies BPE to the previous tokens
tokenizer.apply_bpe_to_dataset(Path("../Datasets/jsfakes-tok/no_bpe"), Path("../Datasets/jsfakes-tok/bpe"))