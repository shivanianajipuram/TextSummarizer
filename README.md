# AI Text Summarization Web App

A transformer-based AI text summarization web application that generates concise summaries from long paragraphs or documents using Natural Language Processing (NLP) and an interactive web interface.

The application helps users summarize lengthy text into meaningful short summaries while preserving important information. It demonstrates the implementation of transformer-based NLP models, text tokenization, sequence processing, and real-time summary generation through a user-friendly Streamlit dashboard.

## Model Used

The project uses the **T5-small Transformer Model** from Hugging Face for abstractive text summarization.

Model used:

T5-small (Text-to-Text Transfer Transformer)

The model is pre-trained on large text datasets and generates summaries by understanding sentence context and key information.

## NLP Techniques Used

- Text Tokenization

- Transformer-based Summarization

- Attention Mechanism

- Context Understanding

- Sequence-to-Sequence Text Generation

- Abstractive Text Summarization

## Tech Stack

### Frontend

- Streamlit

### Backend / Machine Learning

- Python

- Transformers

- PyTorch

- NLP Processing

## Libraries Used

- Streamlit

- Transformers

- Torch

- SentencePiece


## Machine Learning / NLP Model

- T5-small Transformer


## Project Structure
```bash
AITextSummarizer/
│
├── app.py
├── requirements.txt
├── runtime.txt
└── README.md
```
## Features

- Summarizes long paragraphs into concise text

- Real-time text summarization

- Transformer-based NLP processing

- Context-aware summary generation

- Interactive Streamlit dashboard

- Abstractive summarization model

- Fast and user-friendly interface

- Text-to-text generation pipeline

- AI-powered summarization system

## How to Run Locally

Clone the repository

```bash
git clone https://github.com/shivanianajipuram/TextSummarizer.git
```

Open the project folder

```bash
cd TextSummarizer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## Technologies Used

- Python

- Streamlit

- Transformers

- PyTorch

- SentencePiece

- T5-small Transformer

- Natural Language Processing

## Inputs
```bash
Artificial Intelligence is a branch of computer science that enables machines to perform tasks that normally require human intelligence. These tasks include learning from data, understanding language, recognizing images, and making decisions. AI is widely used in healthcare, education, finance, and transportation. It helps automate work, improve accuracy, and save time in many industries.
```
```bash
Climate change refers to long-term changes in global temperature and weather patterns. Human activities such as burning fossil fuels and deforestation increase greenhouse gases in the atmosphere. This leads to rising temperatures, melting glaciers, and extreme weather events. Climate change affects agriculture, wildlife, and human health around the world.
```
```bash
Online education allows students to learn through the internet without being physically present in classrooms. It became more common during the COVID-19 pandemic. Students can attend live classes, watch recorded videos, and complete assignments online. It offers flexibility and easy access to learning resources, but it may also create challenges like internet connectivity issues and reduced face-to-face interaction.
```
```bash
Space exploration is the study of outer space using satellites, spacecraft, and telescopes. Scientists explore planets, stars, and galaxies to understand the universe better. Missions to the Moon and Mars have helped collect valuable scientific information. Space exploration also supports communication systems and weather forecasting on Earth.
```
```bash
Natural Language Processing is a field of Artificial Intelligence that helps computers understand and process human language. It is used in chatbots, translators, voice assistants, and text summarization systems. NLP combines computer science and linguistics to analyze text and speech. It improves communication between humans and machines.
```
Note - We can Expect that the output is summarized and cannot predict the output as we use pre-trained model(t5 transformer)
## Live Demo
```bash
https://textsummarizer-tlagfdashspffda3efkejm.streamlit.app/
```

## The streamlit page looks like this-
<img width="1366" height="674" alt="image" src="https://github.com/user-attachments/assets/f28ec341-6769-4230-98f1-e62dff6357e0" />
