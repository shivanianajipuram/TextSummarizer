import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝"
)

# Load model only once
@st.cache_resource
def load_model():
    return pipeline(
        "summarization",
        model="t5-small",
        tokenizer="t5-small"
    )

summarizer = load_model()

st.title("📝 Text Summarization using Transformer")
st.write("Paste long text and generate summary using T5 model")

text = st.text_area(
    "Enter Text:",
    height=250
)

if st.button("Summarize"):

    if not text.strip():
        st.warning("Please enter some text")

    else:
        with st.spinner("Generating summary..."):

            result = summarizer(
                "summarize: " + text,
                max_length=120,
                min_length=30,
                do_sample=False
            )

            st.subheader("Summary")
            st.success(result[0]["summary_text"])