Bank of Maharashtra RAG Pipeline

Overview
This project implements a lightweight Retrieval-Augmented Generation (RAG) pipeline using data scraped from the Bank of Maharashtra website.
The system enables users to ask natural language questions about different loan schemes (home, car, education, personal, etc.) and receive accurate, factual answers.

The workflow consists of:

-Web scraping of loan data
-Data cleaning and preprocessing
-Building and querying a lightweight RAG pipeline

Setup Instructions
1. Clone the Repository
git clone https://github.com/Alwyna30/BOM_RAG_PIPELINE.git
cd BOM_RAG_PIPELINE

2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Run the Pipeline

Data Scraping
python scripts/scraper.py


Data Cleaning
python scripts/clean_data.py


RAG Pipeline
python scripts/rag_pipeline_code.py


Or use the interactive notebook:

notebooks/Rag_Pipeline_Code.ipynb

Project Structure
BOM_RAG_PIPELINE/
│
├── data/
│   ├── raw/                # Scraped data
│   ├── processed/          # Cleaned data
│   
│
├── scripts/
│   ├── scraper.py
│   ├── clean_data.py
│   └── rag_pipeline_code.py
│
├── notebooks/
│   └── Rag_Pipeline_Code.ipynb
│
├── requirements.txt
└── README.md

Key Design Choices

Libraries
Web Scraping - requests, beautifulsoup4
Data Cleaning -	pandas, nltk
Embeddings - sentence-transformers
Vector Search -	chromadb
Model Inference -	huggingface_hub, torch

Data Strategy
Scraped multiple loan pages (home, car, personal, education, etc.).
Cleaned and chunked text (~800 characters) with loan type tags.
Embedded using Sentence Transformers and stored in ChromaDB.

Models
Embedding Model: all-MiniLM-L6-v2
LLM: Mistral-7B-Instruct via Hugging Face API

Challenges & Solutions
Noisy website text - Targeted HTML divs using BeautifulSoup
Duplicate and irrelevant data -	Regex-based filtering and keyword extraction
LLM hallucinations - Strict prompt template with “Answer only if context available”
Dependency issues -	Fixed by pinning torch==2.2.2+cpu, numpy<2.0

Data Files
data/raw/bom_loan_data.csv - Raw scraped text
data/processed/bom_loan_clean.csv -	Cleaned text for embeddings
data/vector_data/bom_with_embeddings.pkl -	Stored vector embeddings

Walkthrough Video
A 5-minute project walkthrough demonstrating the complete process:
(https://drive.google.com/file/d/1Mhe7qGXl3NLBGEvufRNohlPZlXXsTJvu/view?usp=drive_link)

Author

Name: Alwyna Chandanshiv
Email: chandanshiv.alwyna302@gmail.com


Summary

This project demonstrates an end-to-end RAG pipeline built entirely with open-source tools from scraping and cleaning real banking data to semantic retrieval and LLM-based question answering.