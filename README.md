# A Simple Easy to use Text to Audio Converter for Students

This is a simple tool designed for students who want to convert text from PDF files into audio format. Whether you're multitasking, commuting, or simply prefer auditory learning, this tool aims to make it easier for you to consume textual content on the go.

## Features

- **Effortless PDF Upload**: Simply upload your PDF file, and the tool will take care of the rest.
- **Automatic Text Extraction**: The tool automatically extracts text from the uploaded PDF file.
- **Instant Audio Conversion**: With just a click of a button, the extracted text is converted into audio format.
- **Streamlined Interface**: The user interface is designed to be intuitive and user-friendly, ensuring a hassle-free experience.

## How to Use

1. **Upload PDF File**: Click on the "Upload a PDF file" button to select and upload your PDF document.
2. **Conversion**: Once the PDF is uploaded, click on the "Send" button to initiate the conversion process.
3. **Listen**: Sit back and relax as the tool converts the text into audio format. You can listen to the audio directly from your browser.

## Installation

To run this tool locally, you'll need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install gtts streamlit PyPDF2
```

## Usage

After installing the dependencies, you can run the tool by executing the following command in your terminal:

```bash
streamlit run <filename>.py
```

Replace `<filename>` with the name of the Python script containing the provided code.

## Code

```python
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
```

## Disclaimer

This tool is provided as-is and may have limitations or inaccuracies in text extraction. It's recommended to review the converted audio for accuracy, especially in technical or complex documents.

Feel free to contribute to this project by submitting bug reports or enhancements through GitHub issues. Your feedback is highly appreciated!
