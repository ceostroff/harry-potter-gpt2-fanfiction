from aitextgen.TokenDataset import TokenDataset
from aitextgen.tokenizers import train_tokenizer
from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen

# FIXME: clean the text?
# find data/ -name '*.txt' -exec cat {} \; > data/all_stories.txt
file_name = 'data/all_stories.txt'
vocab_file = 'model/aitextgen-vocab.json'
merges_file = 'model/aitextgen-merges.txt'

train_tokenizer(file_name, save_path="model")

config = GPT2ConfigCPU()
ai = aitextgen(vocab_file=vocab_file,
               merges_file=merges_file, config=config)

data = TokenDataset(file_name, vocab_file=vocab_file,
                    merges_file=merges_file, block_size=64)

# train the model
ai.train(data, output_dir="model", batch_size=16, num_steps=5000)

# run some tests
ai.generate(n=10, prompt="Hermione")
ai.generate_samples(prompt="Hermione")
ai.generate(n=10, prompt="Harry")
ai.generate(n=10, prompt="Ron")
ai.generate(n=10, prompt="Hufflepuff")
