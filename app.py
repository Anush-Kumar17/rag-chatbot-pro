# import sys
# import types

# # Fix for Windows
# sys.modules['pwd'] = types.ModuleType('pwd')

# import streamlit as st
# from utils import load_and_process
# from transformers import pipeline

# # 🔥 Page Config
# st.set_page_config(page_title="RAG Chatbot Pro", layout="wide")

# # 🔥 Styling
# st.markdown("""
# <style>
# .chat-box {
#     background-color: #1e293b;
#     padding: 15px;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }
# .user { color: #38bdf8; font-weight: bold; }
# .bot { color: #22c55e; font-weight: bold; }
# .source { font-size: 12px; color: #94a3b8; }
# </style>
# """, unsafe_allow_html=True)

# # 🔥 Title
# st.title("🤖 RAG Chatbot Pro")
# st.write("Flan-T5 Large + Reasoning 🚀")

# # Upload
# uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

# # Chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if uploaded_file:
#     with open("temp.pdf", "wb") as f:
#         f.write(uploaded_file.read())

#     st.success("✅ PDF Uploaded!")

#     # Load DB
#     db = load_and_process("temp.pdf")

#     # 🔥 LLM (UPGRADED)
#     qa_pipeline = pipeline(
#         "text2text-generation",
#         model="google/flan-t5-large",
#         max_length=512,
#         temperature=0.2,
#         do_sample=False
#     )

#     query = st.text_input("💬 Ask your question")

#     if query:
#         # 🔥 Step 1: Retrieve more docs
#         docs = db.similarity_search(query, k=8)

#         # 🔥 Step 2: Filter
#         filtered_docs = [doc for doc in docs if len(doc.page_content) > 80]
#         top_docs = filtered_docs[:4]

#         context = "\n\n".join([doc.page_content for doc in top_docs])

#         # 🔥 Step 3: Reasoning pass
#         reasoning_prompt = f"""
# You are an expert AI assistant.

# Extract key ideas from the context relevant to the question.

# Context:
# {context}

# Question:
# {query}

# Key Points:
# """

#         reasoning = qa_pipeline(reasoning_prompt)[0]["generated_text"]

#         # 🔥 Step 4: Final answer
#         final_prompt = f"""
# You are a highly accurate AI assistant.

# Use the key points below to answer clearly.

# Rules:
# - Answer ONLY from the context
# - Do NOT hallucinate
# - Be concise and precise

# Key Points:
# {reasoning}

# Question:
# {query}

# Final Answer:
# """

#         result = qa_pipeline(final_prompt)[0]["generated_text"]

#         # 🔥 Clean answer
#         if "Final Answer:" in result:
#             answer = result.split("Final Answer:")[-1].strip()
#         else:
#             answer = result.strip()

#         if len(answer) > 300:
#             answer = answer[:300]

#         # Save chat
#         st.session_state.chat_history.append((query, answer, top_docs))

# # 🔥 Display chat
# for q, a, docs in reversed(st.session_state.chat_history):

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="user">🧑 You:</div>
#         <div>{q}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="bot">🤖 Bot:</div>
#         <div>{a}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.expander("📚 Sources"):
#         for i, doc in enumerate(docs):
#             st.markdown(
#                 f"<div class='source'>Source {i+1}: {doc.page_content[:200]}...</div>",
#                 unsafe_allow_html=True
#             )
# import sys
# import types

# # Fix for Windows (pwd issue)
# sys.modules['pwd'] = types.ModuleType('pwd')

# import streamlit as st
# from utils import load_and_process
# from transformers import pipeline

# # Page setup
# st.set_page_config(page_title="RAG Chatbot Pro", layout="wide")

# # Styling
# st.markdown("""
# <style>
# .chat-box {
#     background-color: #1e293b;
#     padding: 15px;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }
# .user { color: #38bdf8; font-weight: bold; }
# .bot { color: #22c55e; font-weight: bold; }
# .source { font-size: 12px; color: #94a3b8; }
# </style>
# """, unsafe_allow_html=True)

# st.title("🤖 RAG Chatbot Pro")
# st.write("Flan-T5 Large + Smart Reasoning 🚀")

# uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

# # Chat memory
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if uploaded_file:
#     with open("temp.pdf", "wb") as f:
#         f.write(uploaded_file.read())

#     st.success("✅ PDF Uploaded!")

#     db = load_and_process("temp.pdf")

#     # 🔥 IMPROVED MODEL SETTINGS
#     qa_pipeline = pipeline(
#         "text2text-generation",
#         model="google/flan-t5-large",
#         max_new_tokens=300,   # 🔥 more output space
#         temperature=0.7,      # 🔥 smarter answers
#         top_p=0.9,
#         do_sample=True        # 🔥 better reasoning
#     )

#     query = st.text_input("💬 Ask your question")

#     if query:
#         query_lower = query.lower()

#         # 🔥 SMART DETECTION (summary / topics)
#         if any(word in query_lower for word in ["topics", "summary", "overview", "covered"]):

#             docs = db.similarity_search(query, k=20)  # 🔥 more context
#             context = "\n\n".join([doc.page_content for doc in docs[:10]])

#             prompt = f"""
# You are a highly intelligent AI assistant.

# Your task is to carefully read the context and extract ALL important topics.

# Instructions:
# - Identify ALL key topics discussed
# - Do NOT miss any important section
# - Return answer as bullet points
# - Be comprehensive but clear

# Context:
# {context}

# Answer:
# """

#         else:
#             # 🔥 NORMAL QA MODE
#             docs = db.similarity_search(query, k=10)

#             filtered_docs = [doc for doc in docs if len(doc.page_content) > 80]
#             top_docs = filtered_docs[:5]

#             context = "\n\n".join([doc.page_content for doc in top_docs])

#             prompt = f"""
# You are a highly accurate AI assistant.

# Rules:
# - Answer ONLY using the context
# - Do NOT hallucinate
# - Be precise and helpful

# Context:
# {context}

# Question:
# {query}

# Answer:
# """

#         # Generate
#         result = qa_pipeline(prompt)[0]["generated_text"]

#         # Clean answer
#         if "Answer:" in result:
#             answer = result.split("Answer:")[-1].strip()
#         else:
#             answer = result.strip()

#         # 🔥 Force bullet formatting if needed
#         if any(word in query_lower for word in ["topics", "summary", "overview"]):
#             if "-" not in answer:
#                 answer = "\n- " + answer.replace(". ", "\n- ")

#         # Limit size (optional UI control)
#         if len(answer) > 600:
#             answer = answer[:600]

#         # Save
#         st.session_state.chat_history.append((query, answer, docs[:4]))

# # Display chat
# for q, a, docs in reversed(st.session_state.chat_history):

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="user">🧑 You:</div>
#         <div>{q}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="bot">🤖 Bot:</div>
#         <div>{a}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.expander("📚 Sources"):
#         for i, doc in enumerate(docs):
#             st.markdown(
#                 f"<div class='source'>Source {i+1}: {doc.page_content[:200]}...</div>",
#                 unsafe_allow_html=True
#             )
#app.py
# import sys
# import types

# # Fix for Windows (pwd issue)
# sys.modules['pwd'] = types.ModuleType('pwd')

# import streamlit as st
# from utils import load_and_process
# from transformers import pipeline

# # Page setup
# st.set_page_config(page_title="RAG Chatbot Pro", layout="wide")

# # Styling
# st.markdown("""
# <style>
# .chat-box {
#     background-color: #1e293b;
#     padding: 15px;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }
# .user { color: #38bdf8; font-weight: bold; }
# .bot { color: #22c55e; font-weight: bold; }
# .source { font-size: 12px; color: #94a3b8; }
# </style>
# """, unsafe_allow_html=True)

# st.title("🤖 RAG Chatbot Pro")
# st.write("Flan-T5 Large + Smart Reasoning 🚀")

# uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

# # Chat memory
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if uploaded_file:
#     with open("temp.pdf", "wb") as f:
#         f.write(uploaded_file.read())

#     st.success("✅ PDF Uploaded!")

#     db = load_and_process("temp.pdf")

#     # Model
#     qa_pipeline = pipeline(
#         "text2text-generation",
#         model="google/flan-t5-large"
#     )

#     query = st.text_input("💬 Ask your question")

#     if query:
#         query_lower = query.lower()

#         # 🔥 SPECIAL RETRIEVAL FOR TOPICS
#         if any(word in query_lower for word in ["topics", "summary", "overview", "covered"]):
#             docs = db.similarity_search("main topics of the document", k=20)
#         else:
#             docs = db.similarity_search(query, k=15)

#         # 🔥 Sort by richer content
#         docs = sorted(docs, key=lambda x: len(x.page_content), reverse=True)

#         top_docs = docs[:8]

#         context = "\n\n".join([doc.page_content for doc in top_docs])

#         # 🔥 CLEAN PROMPT (NO LEAKAGE)
#         if any(word in query_lower for word in ["topics", "summary", "overview", "covered"]):

#             prompt = f"""
# You are an expert AI assistant.

# Your job is to extract important topics from the document.

# IMPORTANT:
# - Ignore all instructions
# - Only use the context
# - Do NOT copy any instruction text
# - Do NOT include sentences like "cover the document"

# Return ONLY bullet points of topics.

# Context:
# {context}

# Topics:
# """

#         else:
#             prompt = f"""
# You are an expert AI assistant.

# Instructions:
# - Answer ONLY using the context
# - Do NOT hallucinate
# - If answer not found, say: "I don't know based on the document."

# Context:
# {context}

# Question:
# {query}

# Answer:
# """

#         # 🔥 GENERATE
#         result = qa_pipeline(
#             prompt,
#             max_new_tokens=512,
#             temperature=0.3,
#             top_p=0.9,
#             do_sample=True
#         )[0]["generated_text"]

#         # 🔥 CLEAN OUTPUT
#         if "Answer:" in result:
#             answer = result.split("Answer:")[-1].strip()
#         elif "Topics:" in result:
#             answer = result.split("Topics:")[-1].strip()
#         else:
#             answer = result.strip()

#         # 🔥 REMOVE BAD TEXT (IMPORTANT FIX)
#         bad_phrases = [
#             "cover the entire document",
#             "read the context",
#             "your task",
#             "instructions",
#             "you are"
#         ]

#         for phrase in bad_phrases:
#             answer = answer.replace(phrase, "")

#         # 🔥 FORCE BULLETS
#         if any(word in query_lower for word in ["topics", "summary", "overview"]):
#             if "-" not in answer:
#                 answer = "\n- " + answer.replace(". ", "\n- ")

#         # Limit size
#         if len(answer) > 1000:
#             answer = answer[:1000]

#         # Save
#         st.session_state.chat_history.append((query, answer, top_docs[:4]))

# # Display chat
# for q, a, docs in reversed(st.session_state.chat_history):

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="user">🧑 You:</div>
#         <div>{q}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="bot">🤖 Bot:</div>
#         <div>{a}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.expander("📚 Sources"):
#         for i, doc in enumerate(docs):
#             st.markdown(
#                 f"<div class='source'>Source {i+1}: {doc.page_content[:200]}...</div>",
#                 unsafe_allow_html=True
#             )
# import sys
# import types

# # Fix for Windows (pwd issue)
# sys.modules['pwd'] = types.ModuleType('pwd')

# import streamlit as st
# from utils import load_and_process
# from transformers import pipeline
# import time
# import pandas as pd
# import matplotlib.pyplot as plt

# # Page setup
# st.set_page_config(page_title="RAG Chatbot Pro", layout="wide")

# # Styling
# st.markdown("""
# <style>
# .chat-box {
#     background-color: #1e293b;
#     padding: 15px;
#     border-radius: 10px;
#     margin-bottom: 10px;
# }
# .user { color: #38bdf8; font-weight: bold; }
# .bot { color: #22c55e; font-weight: bold; }
# .source { font-size: 12px; color: #94a3b8; }
# </style>
# """, unsafe_allow_html=True)

# st.title("🤖 RAG Chatbot Pro")
# st.write("Flan-T5 Large + Smart AI + Analytics 📊🚀")

# uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

# # Chat memory
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Performance metrics
# if "metrics" not in st.session_state:
#     st.session_state.metrics = []

# # Cache DB
# @st.cache_resource
# def get_db(file):
#     return load_and_process(file)

# if uploaded_file:
#     with open("temp.pdf", "wb") as f:
#         f.write(uploaded_file.read())

#     st.success("✅ PDF Uploaded!")

#     db = get_db("temp.pdf")

#     # Model
#     qa_pipeline = pipeline(
#         "text2text-generation",
#         model="google/flan-t5-large"
#     )

#     # Suggestions
#     st.write("💡 Try asking:")
#     st.write("- What are the key topics?")
#     st.write("- Summarize this document")
#     st.write("- Explain main concepts")

#     # Summary button
#     if st.button("📄 Summarize Document"):
#         with st.spinner("Summarizing..."):
#             docs = db.similarity_search("summary of document", k=15)
#             context = "\n".join([d.page_content for d in docs])

#             result = qa_pipeline(context, max_new_tokens=300)[0]["generated_text"]
#             st.markdown("### 📌 Summary")
#             st.write(result)

#     # Input
#     query = st.text_input("💬 Ask your question")

#     if query:
#         query_lower = query.lower()

#         # Chat history
#         history = "\n".join([
#             f"Q: {q}\nA: {a}" for q, a, _ in st.session_state.chat_history[-3:]
#         ])

#         # Better retrieval (MMR)
#         docs = db.max_marginal_relevance_search(query, k=8)

#         docs = sorted(docs, key=lambda x: len(x.page_content), reverse=True)
#         top_docs = docs[:6]

#         context = "\n\n".join([doc.page_content for doc in top_docs])

#         prompt = f"""
# You are an expert AI assistant.

# Conversation:
# {history}

# Instructions:
# - Answer ONLY from context
# - Be clear and structured
# - If not found, say: "I don't know based on the document."

# Context:
# {context}

# Question:
# {query}

# Answer:
# """

#         # ⏱️ Measure time
#         start_time = time.time()

#         with st.spinner("Thinking..."):
#             result = qa_pipeline(
#                 prompt,
#                 max_new_tokens=400,
#                 temperature=0.4,
#                 top_p=0.9,
#                 do_sample=True
#             )[0]["generated_text"]

#         end_time = time.time()
#         response_time = end_time - start_time

#         # Clean answer
#         if "Answer:" in result:
#             answer = result.split("Answer:")[-1].strip()
#         else:
#             answer = result.strip()

#         # Confidence
#         context_length = len(context)
#         confidence = min(context_length / 1500, 1.0)

#         st.progress(confidence)
#         st.caption("Confidence Score")

#         # Save metrics
#         st.session_state.metrics.append({
#             "query": query,
#             "response_time": response_time,
#             "context_length": context_length,
#             "confidence": confidence
#         })

#         # Save chat
#         st.session_state.chat_history.append((query, answer, top_docs))

# # Display chat
# for q, a, docs in reversed(st.session_state.chat_history):

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="user">🧑 You:</div>
#         <div>{q}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="chat-box">
#         <div class="bot">🤖 Bot:</div>
#         <div>{a}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.expander("📚 Sources"):
#         for i, doc in enumerate(docs):
#             st.markdown(
#                 f"<div class='source'>Source {i+1}: {doc.page_content[:200]}...</div>",
#                 unsafe_allow_html=True
#             )

# # Download chat
# if st.button("⬇ Download Chat"):
#     text = "\n".join([
#         f"Q: {q}\nA: {a}" for q, a, _ in st.session_state.chat_history
#     ])
#     st.download_button("Download", text, file_name="chat.txt")

# # 📊 PERFORMANCE DASHBOARD
# st.markdown("## 📊 Performance Dashboard")

# if st.session_state.metrics:
#     df = pd.DataFrame(st.session_state.metrics)

#     st.metric("Total Queries", len(df))

#     st.write("### ⏱️ Response Time")
#     st.line_chart(df["response_time"])

#     st.write("### 📄 Context Length")
#     st.line_chart(df["context_length"])

#     st.write("### 📊 Confidence Score")
#     st.line_chart(df["confidence"])

#     # Custom graph
#     fig, ax = plt.subplots()
#     ax.plot(df["response_time"], label="Response Time")
#     ax.plot(df["confidence"], label="Confidence")
#     ax.legend()
#     ax.set_title("Performance Overview")

#     st.pyplot(fig)
import sys
import types

# Fix for Windows (pwd issue)
sys.modules['pwd'] = types.ModuleType('pwd')

import streamlit as st
from utils import load_and_process
from transformers import pipeline
import time
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="RAG Chatbot Pro", layout="wide")

# 🔥 ADVANCED UI STYLING (CHATGPT STYLE)
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

/* Cards */
.card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(56,189,248,0.2);
    text-align: center;
    margin: 10px;
}

/* Glow text */
.glow {
    color: #38bdf8;
    text-shadow: 0 0 10px #38bdf8;
}

/* Chat box */
.chat-box {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}

.user { color: #38bdf8; font-weight: bold; }
.bot { color: #22c55e; font-weight: bold; }
.source { font-size: 12px; color: #94a3b8; }

</style>
""", unsafe_allow_html=True)

st.title("🤖 RAG Chatbot Pro")
st.write("Flan-T5 Large + Smart AI + Analytics 🚀")

uploaded_file = st.file_uploader("📄 Upload PDF", type="pdf")

# Chat memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Metrics storage
if "metrics" not in st.session_state:
    st.session_state.metrics = []

# Cache DB
@st.cache_resource
def get_db(file):
    return load_and_process(file)

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF Uploaded!")

    db = get_db("temp.pdf")

    # Model
    qa_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-large"
    )

    st.write("💡 Try asking:")
    st.write("- What are the key topics?")
    st.write("- Summarize this document")
    st.write("- Explain main concepts")

    # Input
    query = st.text_input("💬 Ask your question")

    if query:
        history = "\n".join([
            f"Q: {q}\nA: {a}" for q, a, _ in st.session_state.chat_history[-3:]
        ])

        docs = db.max_marginal_relevance_search(query, k=8)
        docs = sorted(docs, key=lambda x: len(x.page_content), reverse=True)
        top_docs = docs[:6]

        context = "\n\n".join([doc.page_content for doc in top_docs])

        prompt = f"""
You are an expert AI assistant.

Conversation:
{history}

Instructions:
- Answer ONLY from context
- Be clear and structured
- If not found, say: "I don't know based on the document."

Context:
{context}

Question:
{query}

Answer:
"""

        # ⏱️ TIME (FIXED)
        start_time = time.time()

        with st.spinner("Thinking..."):
            result = qa_pipeline(
                prompt,
                max_new_tokens=400,
                temperature=0.4,
                top_p=0.9,
                do_sample=True
            )[0]["generated_text"]

        end_time = time.time()

        # 🔥 FIXED METRICS
        response_time = round((end_time - start_time) * 1000, 2)  # ms
        context_length = sum(len(doc.page_content) for doc in top_docs)
        confidence = round(context_length / 5000, 2)
        confidence = min(confidence, 1.0)

        # Clean answer
        if "Answer:" in result:
            answer = result.split("Answer:")[-1].strip()
        else:
            answer = result.strip()

        # Show confidence
        st.progress(confidence)
        st.caption(f"Confidence Score: {confidence}")

        # Store metrics
        st.session_state.metrics.append({
            "response_time": float(response_time),
            "context_length": int(context_length),
            "confidence": float(confidence)
        })

        # Save chat
        st.session_state.chat_history.append((query, answer, top_docs))

# Chat display
for q, a, docs in reversed(st.session_state.chat_history):

    st.markdown(f"""
    <div class="chat-box">
        <div class="user">🧑 You:</div>
        <div>{q}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="chat-box">
        <div class="bot">🤖 Bot:</div>
        <div>{a}</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📚 Sources"):
        for i, doc in enumerate(docs):
            st.markdown(
                f"<div class='source'>Source {i+1}: {doc.page_content[:200]}...</div>",
                unsafe_allow_html=True
            )

# 📊 DASHBOARD (CHATGPT STYLE)
st.markdown("## 📊 AI Analytics Dashboard")

if st.session_state.metrics:
    df = pd.DataFrame(st.session_state.metrics)

    avg_time = round(df["response_time"].mean(), 2)
    avg_conf = round(df["confidence"].mean(), 2)
    avg_context = int(df["context_length"].mean())

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"""
    <div class="card">
        <h3>📌 Total Queries</h3>
        <h1 class="glow">{len(df)}</h1>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class="card">
        <h3>⏱ Avg Response</h3>
        <h1 class="glow">{avg_time} ms</h1>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="card">
        <h3>📄 Avg Context</h3>
        <h1 class="glow">{avg_context}</h1>
    </div>
    """, unsafe_allow_html=True)

    col4.markdown(f"""
    <div class="card">
        <h3>📊 Confidence</h3>
        <h1 class="glow">{avg_conf}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📈 Performance Trends")

    colA, colB = st.columns(2)

    with colA:
        st.line_chart(df["response_time"])

    with colB:
        st.line_chart(df["confidence"])

    st.line_chart(df["context_length"])

    # Advanced graph
    fig, ax = plt.subplots()

    ax.plot(df.index, df["response_time"], marker='o', label="Response Time (ms)")
    ax.plot(df.index, df["confidence"], marker='x', label="Confidence")

    ax.set_facecolor("#0f172a")
    fig.patch.set_facecolor("#0f172a")

    ax.set_title("Performance Overview", color="white")
    ax.tick_params(colors='white')
    ax.legend()
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)