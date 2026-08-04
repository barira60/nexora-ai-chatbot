# 🤖 Nexora AI Assistant

Nexora AI Assistant is a local AI-powered chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions from company documents. Instead of relying on general knowledge, it searches a custom knowledge base and generates accurate responses using a local Large Language Model (LLM).

---

## 🚀 Features

- AI-powered question answering
- Retrieval-Augmented Generation (RAG)
- Local Llama 3.2 model using Ollama
- FAISS vector database
- HuggingFace embeddings
- Supports TXT and Excel files
- Modern Streamlit user interface
- Answers only from the provided knowledge base
- Prevents AI hallucinations by responding "I don't know" when information is unavailable

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- Ollama
- Llama 3.2

---

## 📂 Project Structure

```
nexora-ai-chatbot/
│
├── app.py
├── rag.py
├── requirements.txt
├── .env
├── data/
│   ├── company_info.txt
│   └── products.xlsx
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/barira60/nexora-ai-chatbot.git
```

### 2. Open the project

```bash
cd nexora-ai-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### 5. Install Python packages

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from

https://ollama.com/download

---

## Download the Llama 3.2 model

```bash
ollama pull llama3.2
```

---

## Start Ollama

```bash
ollama serve
```

---

## Run the application

```bash
streamlit run app.py
```

---

## Example Questions

- What products does the company offer?
- What are the prices of the products?
- Tell me about the company.
- What services are available?
- What is the refund policy?

---

## How It Works

1. Documents are loaded from the data folder.
2. The documents are split into smaller chunks.
3. HuggingFace creates embeddings.
4. FAISS stores the embeddings.
5. User asks a question.
6. Relevant document chunks are retrieved.
7. Llama 3.2 (running locally through Ollama) generates the final answer.

---

## Future Improvements

- PDF support
- Chat history export
- Multiple document upload
- Voice input
- User authentication

---

## Author

**Barira Babar**

Fresh Graduate | AI & Python Developer

LinkedIn:
www.linkedin.com/in/barira-babar