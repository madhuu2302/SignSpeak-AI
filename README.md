SignSpeak AI

SignSpeak AI is an AI-powered signboard understanding system using Tesseract OCR and a Hugging Face LLM. It extracts text from signboard images and provides simple explanations and English/Tamil translations.
Application:http://localhost:8502/

Features

Upload signboard images
Text extraction using Tesseract OCR
AI-based sign understanding
Sign category and meaning
Important information
Suggested action
English and Tamil translation

Technologies
Python
Streamlit
Tesseract OCR
Pillow
Hugging Face
python-dotenv

Workflow
Image
  ↓
Tesseract OCR
  ↓
Extracted Text
  ↓
Hugging Face LLM
  ↓
Meaning + Category + Translation

Run

Install dependencies:
pip install -r requirements.txt

Run the application:
python -m streamlit run app.py

Project Architecture
                ┌─────────────────┐
                │  Signboard Image│
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │    Streamlit    │
                │       UI        │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │  Image          │
                │  Preprocessing  │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Tesseract OCR   │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │  Extracted Text │
                └────────┬────────┘
                         ↓
                ┌─────────────────┐
                │ Hugging Face LLM│
                └────────┬────────┘
                         ↓
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Category       Explanation     Translation
                                         │
                                  ┌──────┴──────┐
                                  ↓             ↓
                               English       Tamil

Conclusion
SignSpeak AI demonstrates how OCR and Large Language Models can work together to make signboards and public notices easier to understand. Tesseract extracts the text,while the Hugging Face LLM interprets
the extracted content and provides structured explanations and translations.
