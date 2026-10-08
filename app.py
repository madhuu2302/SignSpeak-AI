import streamlit as st
from PIL import Image
from ocr import extract_text
from llm import analyze_sign

st.set_page_config(
    page_title="SignSpeak AI",
    page_icon="🚦",
    layout="centered"
)

st.title("🚦 SignSpeak AI")
st.write(
    "AI-powered signboard and public notice "
    "understanding system"
)

uploaded_file = st.file_uploader(
    "📷 Upload a signboard image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(
        image,
        caption="Uploaded Sign",
        use_container_width=True
    )
    if st.button("🔍 Analyze Sign"):
        with st.spinner("🔍 Extracting text..."):
            text = extract_text(image)
        st.subheader("🔍 Extracted Text")

        if text:
            st.code(text)
            with st.spinner(
                "🤖 SignSpeak AI is understanding the sign..."
            ):
                try:
                    result = analyze_sign(text)

                    st.subheader(
                        "🤖 SignSpeak AI Analysis"
                    )
                    st.markdown(result)
                except Exception as e:
                    st.error(
                        "Unable to connect to the AI model."
                    )

                    st.code(str(e))


        else:
            st.warning(
                "⚠️ No text detected. "
                "Please upload a clearer signboard image."
            )
