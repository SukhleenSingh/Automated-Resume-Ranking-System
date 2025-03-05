import pdfplumber
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Rank resumes based on similarity
def rank_resumes(job_description, resumes):
    documents = [job_description] + [resume["text"] for resume in resumes]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    ranked_resumes = sorted(
        [{"name": resumes[i]["name"], "score": round(similarity_scores[i] * 100, 2)}
         for i in range(len(resumes))],
        key=lambda x: x["score"], reverse=True
    )

    return ranked_resumes
