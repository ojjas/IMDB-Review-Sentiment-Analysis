import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tokenizer import tokenizer, max_length, trunc_type
import streamlit as st
import numpy as np

st.title('Movie Review Sentiment Analysis')
st.write("This ML model will guess if a given review is positive or negative by using NLP. "
         "This model was trained using Tensorflow and was trained on the imdb-dataset of movie reviews.")

@st.cache(allow_output_mutation=True)
def load_model():
    new_model = tf.keras.models.load_model('text_model.hdf5')
    return new_model
new_text_model = load_model()
pred_review_text = st.text_input("Enter your review")

if pred_review_text != '':
    pred = []
    pred.append(pred_review_text)

    with st.spinner("Tokenizing Text....."):
        pred_seq = tokenizer.texts_to_sequences(pred)
        pred_padded = pad_sequences(pred_seq, maxlen=max_length, truncating=trunc_type)

    val = new_text_model.predict(pred_padded)
    new_val = str(val)
    st.subheader("The given review is : ")
    if val > [[0.5]]:
        st.write("Positive")
    else:
        st.write("Negative")