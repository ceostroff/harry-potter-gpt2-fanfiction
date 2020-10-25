from aitextgen.utils import GPT2ConfigCPU
from aitextgen import aitextgen

config = GPT2ConfigCPU()

# load the model
ai = aitextgen(model="model/pytorch_model.bin",
               vocab_file='model/aitextgen-vocab.json', merges_file='model/aitextgen-merges.txt', config=config)

# just generate text!
ai.generate(n=10, prompt="Hermione:")
ai.generate(n=10, prompt="Harry")
ai.generate(n=10, prompt="Dobby")
ai.generate(n=10, prompt="Dumbledore", temperature=0.7)
ai.generate(n=10, prompt="Dumbledore", temperature=0.9)

ai.generate_to_file(n=100, prompt="Hufflepuff",
                    temperature=0.8, destination_path="output/hufflepuff_100.txt")
ai.generate_to_file(n=100, prompt="Hermione",
                    temperature=0.9, destination_path="output/hermione_100.txt")
ai.generate_to_file(n=100, prompt="Harry",
                    temperature=1, destination_path="output/harry_100.txt")
