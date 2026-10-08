import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)
def analyze_sign(text):

    prompt = f"""
You are SignSpeak AI, an AI assistant that understands
signboards and public notices.

Analyze the following OCR text:

{text}

Your task is to explain the sign clearly.

IMPORTANT RULES:

1. Do not invent information.
2. Use only information that can reasonably be obtained
   from the OCR text.
3. Do not assume information about authorities, penalties,
   accidents, road conditions, maintenance, or laws unless
   it is explicitly present.
4. The OCR may contain spelling mistakes.
5. If the OCR text is unclear, mention:
   "OCR may be inaccurate."
6. ALWAYS provide an English translation.
7. ALWAYS provide a Tamil translation.
8. Keep the answer short and simple.
9. Do not leave any section empty.

Return EXACTLY in this format:

CATEGORY:
Give the likely category of the sign.

SIMPLE MEANING:
Explain the sign in simple English.

IMPORTANT INFORMATION:
Mention only important information present in the text.

WHAT SHOULD I DO:
Explain the action suggested by the sign.
If no action can be determined, write:
"No specific action can be determined from the OCR text."

ENGLISH TRANSLATION:
Give the English translation of the detected text.

TAMIL TRANSLATION:
Give the Tamil translation in simple Tamil.

OCR TEXT:
{text}
"""
    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        max_tokens=800
    )

    return response.choices[0].message.content
