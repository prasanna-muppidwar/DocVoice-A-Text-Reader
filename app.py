from gtts import gTTS
import streamlit as st
import PyPDF2
import io

from PyPDF2 import PdfReader

def read_pdf(uploaded_file):
    file_buffer = io.BytesIO(uploaded_file.read())
    pdf_reader = PdfReader(file_buffer)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    st.audio("output.mp3", format='audio/mp3')

def main():
    st.title("Lazy Coder's PDF Reader")

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        st.write("Uploaded PDF file:", uploaded_file.name)

        if st.button("Send"):
            text = read_pdf(uploaded_file)
            speak_text(text)

if __name__ == "__main__":
    main()
