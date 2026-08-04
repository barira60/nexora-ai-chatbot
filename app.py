import streamlit as st
from rag import create_rag_chain, ask_question

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Nexora AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Hide Streamlit */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header{visibility:hidden;}

/* Background */
.stApp{
    background:linear-gradient(180deg,#eef4ff,#f8fbff);
}

/* ==========================
   SIDEBAR
========================== */

/* REPLACE YOUR OLD SIDEBAR CSS WITH THIS */
section[data-testid="stSidebar"]{
    background:#111827 !important;
    min-width:320px !important;
    max-width:320px !important;
}

section[data-testid="stSidebar"] > div{
    background:#111827 !important;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Sidebar button */
[data-testid="stSidebar"] .stButton > button{
    width:100% !important;
    background:#2563eb !important;
    color:white !important;
    border:none !important;
    border-radius:10px !important;
    padding:10px !important;
}

[data-testid="stSidebar"] .stButton > button:hover{
    background:#1d4ed8 !important;
}


/* ======================
HERO
====================== */

.hero{
background:linear-gradient(135deg,#0f172a,#2563eb);
padding:25px;
border-radius:24px;
color:white;
margin-bottom:30px;
box-shadow:0 20px 45px rgba(37,99,235,.25);
}

.hero h1{
font-size:40px;
margin:0;
}

.hero p{
opacity:.92;
font-size:17px;
}

/* ======================
CARDS
====================== */

.card{
background:white;
    padding:16px;
    min-height:140px;
}
border-radius:18px;
box-shadow:0 10px 25px rgba(0,0,0,.08);
transition:.3s;
border:1px solid #e5e7eb;
}

.card:hover{
transform:translateY(-5px);
box-shadow:0 18px 40px rgba(0,0,0,.12);
}

.card h3{
margin-bottom:8px;
}

.card p{
color:#64748b;
}

/* ======================
METRICS
====================== */

.metric{
background:white;
padding:18px;
border-radius:18px;
text-align:center;
box-shadow:0 8px 20px rgba(0,0,0,.08);
}

.metric h2{
color:#2563eb;
margin-bottom:5px;
}

/* ======================
CHAT
====================== */

[data-testid="stChatMessage"]{
background:white;
padding:15px;
border-radius:16px;
box-shadow:0 4px 15px rgba(0,0,0,.05);
margin-bottom:12px;
}

/* ======================
CHAT INPUT
====================== */

[data-testid="stChatInput"] > div{
border:2px solid #dbeafe !important;
border-radius:18px !important;
background:white;
}

[data-testid="stChatInput"] > div:focus-within{
border:2px solid #2563eb !important;
box-shadow:0 0 0 4px rgba(37,99,235,.15);
}

[data-testid="stChatInput"] textarea{
outline:none !important;
box-shadow:none !important;
border:none !important;
}

/* ======================
BUTTONS
====================== */

.stButton button{
transition:.25s;
}

.stButton button:hover{
transform:translateY(-2px);
}

/* ======================
FOOTER
====================== */

.footer{
margin-top:40px;
padding:20px;
text-align:center;
color:#64748b;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)
# -----------------------------
# LOAD RAG SYSTEM ONCE
# -----------------------------
@st.cache_resource
def load_rag():
    return create_rag_chain()

retriever, llm = load_rag()

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.markdown("## 🤖 Nexora AI")
    st.success("🟢 System Online")

    st.markdown("---")

    st.markdown("### 📚 Knowledge Base")
    st.write("📄 Company Information")
    st.write("📊 Product Database")
    

    st.markdown("---")

    st.markdown("### ⚙️ AI Stack")
    st.info("""
**LLM:** Llama 3.2

**Embeddings:** HuggingFace

**Vector DB:** FAISS

**Framework:** LangChain

**Frontend:** Streamlit
""")

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown("""
<div class="hero">

<h1>🤖 Nexora AI Assistant</h1>


</div>
""", unsafe_allow_html=True)



# -----------------------------
# SUGGESTED QUESTIONS
# -----------------------------
st.markdown("### 💡 Suggested Questions")

q1, q2, q3, q4 = st.columns(4)

with q1:
    if st.button("🏢 What services do you provide?"):
        st.session_state["question"] = "What services do you provide?"

with q2:
    if st.button("💰 Tell me about pricing"):
        st.session_state["question"] = "Tell me about pricing"

with q3:
    if st.button("📞 Contact information"):
        st.session_state["question"] = "Contact information"

with q4:
    if st.button("📦 What products are available?"):
        st.session_state["question"] = "What products are available?"

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# CHAT HISTORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(
        message["role"],
        avatar="👤" if message["role"] == "user" else "🤖"
    ):
        st.markdown(message["content"])

# -----------------------------
# CHAT INPUT
# -----------------------------
question = st.chat_input("Ask something about Nexora AI...")

if not question and "question" in st.session_state:
    question = st.session_state.pop("question")

if question:

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("🔍 Searching knowledge base..."):

            answer = ask_question(
                question,
                retriever,
                llm
            )

        st.markdown(answer)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

# -----------------------------
# ABOUT SECTION
# -----------------------------
with st.expander("ℹ️ About Nexora AI"):

    st.write("""
This chatbot is powered by:

- **LangChain**
- **FAISS Vector Store**
- **HuggingFace Embeddings**
- **Ollama (Llama 3.2)**
- **Streamlit UI**

It uses **Retrieval-Augmented Generation (RAG)** to answer questions
from your private company knowledge base.
""")

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""

""", unsafe_allow_html=True)