import streamlit as st
from PIL import Image

from ocr import extract_text
from llm import analyze_sign


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="SignSpeak AI",
    page_icon="🚦",
    layout="centered"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚦 SignSpeak AI")

st.write(
    "AI-powered signboard and public notice "
    "understanding system"
)


# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "📷 Upload a signboard image",
    type=["jpg", "jpeg", "png"]
)


# --------------------------------------------------
# PROCESS IMAGE
# --------------------------------------------------

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Sign",
        use_container_width=True
    )


    # --------------------------------------------------
    # ANALYZE BUTTON
    # --------------------------------------------------

    if st.button("🔍 Analyze Sign"):

        # ----------------------------------------------
        # OCR
        # ----------------------------------------------

        with st.spinner("🔍 Extracting text..."):

            text = extract_text(image)


        # ----------------------------------------------
        # DISPLAY OCR TEXT
        # ----------------------------------------------

        st.subheader("🔍 Extracted Text")


        if text:

            st.code(text)


            # ------------------------------------------
            # LLM ANALYSIS
            # ------------------------------------------

            with st.spinner(
                "🤖 SignSpeak AI is understanding the sign..."
            ):

                try:

                    result = analyze_sign(text)


                    # ----------------------------------
                    # DISPLAY RESULT
                    # ----------------------------------

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