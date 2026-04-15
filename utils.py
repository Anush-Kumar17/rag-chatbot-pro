# import sys
# import types

# # Fix for Windows (blocks Linux-only pwd module)
# #sys.modules['langchain_community'] = types.ModuleType('langchain_community')
# sys.modules['pwd'] = types.ModuleType('pwd')

# import sys
# import types

# # 🔥 Fix for Windows (pwd error)
# sys.modules['pwd'] = types.ModuleType('pwd')

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# def load_and_process(pdf_path):
#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()

#     # 🔥 Better chunking (important for accuracy)
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100
#     )
#     chunks = splitter.split_documents(documents)

#     # 🔥 Better embeddings
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )

#     db = FAISS.from_documents(chunks, embeddings)

#     return db
# import sys
# import types

# # Fix for Windows (pwd error)
# sys.modules['pwd'] = types.ModuleType('pwd')

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# def load_and_process(pdf_path):
#     # Load PDF
#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()

#     # 🔥 Better chunking
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100
#     )
#     chunks = splitter.split_documents(documents)

#     # 🔥 Embeddings
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-MiniLM-L6-v2"
#     )

#     # 🔥 Vector DB
#     db = FAISS.from_documents(chunks, embeddings)

#     return db
#utils.py
# import sys
# import types

# # Fix for Windows (pwd error)
# sys.modules['pwd'] = types.ModuleType('pwd')

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# def load_and_process(pdf_path):
#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()

#     # 🔥 Better chunking
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100
#     )
#     chunks = splitter.split_documents(documents)

#     # 🔥 Better embeddings (high accuracy)
#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-mpnet-base-v2"
#     )

#     db = FAISS.from_documents(chunks, embeddings)

#     return db
# import sys
# import types

# sys.modules['pwd'] = types.ModuleType('pwd')

# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS


# def load_and_process(pdf_path):
#     loader = PyPDFLoader(pdf_path)
#     documents = loader.load()

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=800,
#         chunk_overlap=100
#     )
#     chunks = splitter.split_documents(documents)

#     embeddings = HuggingFaceEmbeddings(
#         model_name="sentence-transformers/all-mpnet-base-v2"
#     )

#     db = FAISS.from_documents(chunks, embeddings)

#     return db
import sys
import types

sys.modules['pwd'] = types.ModuleType('pwd')

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def load_and_process(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    db = FAISS.from_documents(chunks, embeddings)

    return db