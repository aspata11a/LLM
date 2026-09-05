import re
from tokenizerClass import SimpleTokenizerV1
from tokenizerClassV2 import SimpleTokenizerV2

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

tokenizer = SimpleTokenizerV2(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2)) 

print(text)

print(tokenizer.encode(text))
#print(ids)
print(tokenizer.decode(tokenizer.encode(text)))

