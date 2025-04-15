# Personalized Patient Education App

This application provides **personalized, layperson-friendly explanations** for medical diagnoses and lab reports. It leverages a **Retrieval-Augmented Generation (RAG)** pipeline using open-source tools to explain complex medical data in simple terms.

---

## 📋 **Features**

- **Input**: Users can upload **PDFs** containing lab reports or enter a medical diagnosis.
- **Retrieve**: The app pulls relevant information from **trusted medical sources** (e.g., MedlinePlus, PubMed).
- **Generate**: The app generates **clear explanations** for medical diagnoses and lab values.
- **Frontend**: Simple web interface built with **Streamlit** for user-friendly interaction.
- **Backend**: The app uses a **RAG pipeline** built with **LangChain**, **FAISS**, and Hugging Face models.

---

## ⚙️ **Tech Stack**

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Embedding Model**: [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss)
- **Generative Model**: [google/flan-t5-base](https://huggingface.co/google/flan-t5-base)
- **Document Store**: Markdown or JSON files with trusted health content
- **Backend**: Python, [LangChain](https://www.langchain.com/)

---

## 🛠️ **Installation & Setup**

### Prerequisites

Ensure you have **Python 3.9+** installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/patient-education-rag.git
cd patient-education-rag
