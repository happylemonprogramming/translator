import requests
import time
import os
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/t5-base"
API_KEY = os.environ["huggingfaceapikey"]
headers = {"Authorization": f"Bearer {API_KEY}"}

st.title('Translator')

inputlang = st.selectbox('Input Language:', ('English','German','French','Romanian'))
outputlang = st.selectbox('Output Language:', ('English','German','French','Romanian'))
if inputlang == outputlang:
	st.error('Please choose different languages')
prompt = st.text_input('Submit Content')

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

if prompt:
    start = time.time()
    payload = {"inputs": f"translate {inputlang} to {outputlang}: {prompt}",}
    print(payload)
    while True:
        output = query(payload)
        if 'error' not in output:
            st.code(output[0]["translation_text"])
            break
        if (time.time()-start) > 36:
            st.error(output)
            break