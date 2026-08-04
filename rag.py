from dotenv import load_dotenv

from langchain_community.document_loaders import (
    TextLoader,
    UnstructuredExcelLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

# Load .env
load_dotenv()


def load_documents():
    """
    Load TXT and Excel files.
    """

    txt_loader = TextLoader(
        "data/company_info.txt",
        encoding="utf-8"
    )

    excel_loader = UnstructuredExcelLoader(
        "data/products.xlsx",
        mode="elements"
    )

    txt_docs = txt_loader.load()
    excel_docs = excel_loader.load()

    return txt_docs + excel_docs


def create_vector_store():
    """
    Create FAISS vector database.
    """

    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    print(f"Loaded {len(documents)} documents")
    print(f"Created {len(chunks)} chunks")

    # FREE Hugging Face Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    print("FAISS vector store created successfully.")

    return vector_store


def create_rag_chain():
    """
    Create Retriever + Ollama LLM.
    """

    vector_store = create_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    return retriever, llm


def ask_question(question, retriever, llm):
    """
    Answer questions using retrieved company data only.
    """

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are the internal AI assistant for Nexora AI Solutions.

Answer ONLY using the context below.

Rules:
1. Do NOT use outside knowledge.
2. Do NOT guess.
3. If the answer is not found in the context, reply exactly:
I don't know.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    print("Creating RAG system...")

    retriever, llm = create_rag_chain()

    print("\nRAG Chatbot Ready!")

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_question(
            question,
            retriever,
            llm
        )

        print("\nAnswer:")
        print(answer)