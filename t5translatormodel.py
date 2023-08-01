import time
import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small', return_dict=True)

# Streamlit Webapp Setup
st.title('Translator')
inputlang = st.selectbox('Input Language:', ('English','German','French','Romanian'))
outputlang = st.selectbox('Output Language:', ('English','German','French','Romanian'))
if inputlang == outputlang:
	st.error('Please choose different languages')
prompt = st.text_input('Submit Content')

# Begin action if user gives prompt
if prompt:
    # Start timeout for error detection
    start = time.time()

    # Initiate translation from prompt
    input_ids = tokenizer(f"translate {inputlang} to {outputlang}: "+prompt, return_tensors="pt").input_ids  # Batch size 1
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Display translation and allow copy
    st.code(decoded)