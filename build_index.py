from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS
import sys

# Load markdown files from the docs folder
loader = DirectoryLoader('docs', glob="**/*.md", loader_cls=TextLoader)
docs = loader.load()

# Check if any documents were loaded
if not docs:
    print("No markdown files found in 'docs' directory. Please check the folder and try again.")
    sys.exit()

# Split documents into smaller chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
split_docs = splitter.split_documents(docs)

# Check again if the splitter returned any chunks
if not split_docs:
    print("Documents were loaded but couldn't be split. Check content or format.")
    sys.exit()

# Create embeddings and build FAISS index
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(split_docs, embedding_model)

# Save the index
vectorstore.save_local("vectorstore/faiss_index")
print("FAISS index built and saved successfully.")
