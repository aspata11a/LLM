import re
from tokenizerClass import SimpleTokenizerV1

with open("the-verdict.txt", "r", encoding="utf-8") as f:
     raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))

#print(preprocessed[:30])

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("Vocab Size:", vocab_size)


# pg. 25
# Creating a vocabulary
vocab = {token:integer for integer,token in enumerate(all_words)}

tokenizer = SimpleTokenizerV1(vocab)

text = """"It's the last he painted, you know,"
       Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print(ids)
print(tokenizer.decode(ids))


#for i, item in enumerate(vocab.items()):
#  print(item)
#  if i >= 5000:
#    break
