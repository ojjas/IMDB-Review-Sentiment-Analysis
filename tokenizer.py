import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
import pandas as pd

col_names = ['Text', 'Label']
train_data = pd.read_csv('Train.csv', names=col_names)

train_text = train_data.Text.tolist()
train_text.pop(0)

top_words = 20000
embedding_vec_length = 32
max_length = 600
trunc_type = 'post'
oov_tok = '<OOV>'

tokenizer = Tokenizer(num_words=top_words, oov_token=oov_tok)
tokenizer.fit_on_texts(train_text)