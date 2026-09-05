import re
from tokenizerClass import SimpleTokenizerV1

with open("the-verdict.txt", "r", encoding="utf-8") as f:
     raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

# all_words = sorted(set(preprocessed))
vocab_size = len(all_tokens)
print("Vocab Size:", vocab_size)


# pg. 25
# Creating a vocabulary
vocab = {token:integer for integer,token in enumerate(all_tokens)}

tokenizer = SimpleTokenizerV1(vocab)

text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))

print("--------------------------Break--------------------")

for i, item in enumerate(list(vocab.items())[-5:]) :
    print(item)
