# Report Analyzer with RAG and Llama 3
This project is a report analysis application built using Retrieval-Augmented Generation (RAG) and the Llama 3 language model. The application enables users to upload PDF documents, extracts text, and allows them to interactively query the content through a conversational AI interface.
## Features
-- PDF Upload and Processing: Upload one or more PDF files and extract the content for analysis.
-- Text Splitting and Embedding: Extracted text is split into manageable chunks and embedded using the OllamaEmbeddings model.
-- Chroma Vector Store: Store text chunks and their embeddings for efficient document retrieval.
-- Conversational Interface: Use Llama 3 integrated with Chainlit to provide an interactive chat interface where users can ask questions about the documents.
-- Contextual Memory: The application remembers the conversation context to provide more accurate and relevant responses.
## Installation
### Clone the repo
```
git clone https://github.com/yourusername/report-analyzer.git
cd report-analyzer

```
### Install Dependencies
```
pip install -r requirements.txt

```
Create a ```.env file``` in the root directory and add your Groq API key:
```
GROQ_API_KEY=your-groq-api-key-here

```
