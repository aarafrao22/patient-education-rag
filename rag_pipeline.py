from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from transformers import pipeline
from langchain.llms import HuggingFacePipeline

# Load embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load FAISS index
db = FAISS.load_local("vectorstore/faiss_index", embeddings, allow_dangerous_deserialization=True)
# Load generator
generator = pipeline("text2text-generation", model="google/flan-t5-base", max_length=256)
llm = HuggingFacePipeline(pipeline=generator)

# Create Prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="Answer the following question in simple language for a patient.\n\nContext:\n{context}\n\nQuestion:\n{question}"
)

# RAG Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=db.as_retriever(),
    chain_type_kwargs={"prompt": prompt}
)

