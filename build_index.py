import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load files
loader = DirectoryLoader("data", glob="**/*.md", loader_cls=TextLoader)
docs = loader.load()

# Split content
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# Embed chunks
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(chunks, embedding_model)

# Save index
os.makedirs("vectorstore", exist_ok=True)
db.save_local("vectorstore/faiss_index")
