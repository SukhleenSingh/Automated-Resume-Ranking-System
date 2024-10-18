import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from transformers import pipeline
import numpy as np

# Load pre-trained Spacy model for NLP processing
nlp = spacy.load('en_core_web_md')

# Preprocessing function (tokenization, lemmatization, removing stopwords)
def preprocess(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Sample job description and resumes
job_description = preprocess("Looking for a software engineer with experience in Python, Django, and SQL.")
resumes = [
    preprocess("Software engineer skilled in Python, Django, SQL, and web development."),
    preprocess("Python developer with experience in Flask, machine learning, and data analysis."),
    preprocess("Experienced backend developer with knowledge of Ruby on Rails, JavaScript, and MySQL.")
]

# Convert text to numerical vectors using TF-IDF
vectorizer = TfidfVectorizer()
all_texts = [job_description] + resumes  # Combine JD and resumes
tfidf_matrix = vectorizer.fit_transform(all_texts)  # Vectorization

# Calculate similarity between JD and each resume
similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

# Print similarity scores (for initial ranking based on similarity)
print("Similarity Scores:", similarity_scores)

# Creating labels (assumed relevance scores for training purposes)
# In a real-world scenario, these labels would come from domain experts or historical data
y = [0.9, 0.7, 0.4]  # Example scores for resumes

# Train a RandomForest model to predict relevance scores based on vectorized input
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix[1:].toarray(), y, test_size=0.2)

# Train RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Predict relevance scores for test data (for unseen resumes)
predicted_scores = model.predict(X_test)
print("Predicted Relevance Scores:", predicted_scores)

# AIOps: System Performance Monitoring with Anomaly Detection
# Simulate system response times (e.g., time taken to process resumes)
response_times = [0.12, 0.15, 0.2, 2.0, 0.14, 0.18]  # Simulated response times in seconds

# Detect anomalies using Isolation Forest
anomaly_detector = IsolationForest(contamination=0.1)
anomalies = anomaly_detector.fit_predict(np.array(response_times).reshape(-1, 1))

# Check for anomalies and print alert if detected
if -1 in anomalies:
    print("Anomaly detected in system performance!")

# (Optional) LLMOps: Use transformer models to provide feedback on resumes
qa_pipeline = pipeline("question-answering")

# Example feedback generation using a transformer model (based on similarity with JD)
context = "The resume contains experience in Python, Django, and SQL."
question = "What is missing from the resume based on the job description?"
result = qa_pipeline(question=question, context=context)

# Output feedback from the LLM
print("LLM Feedback:", result['answer'])

# Final Output: Resume Ranking and Similarity Scores
ranked_resumes = sorted(zip(resumes, similarity_scores), key=lambda x: x[1], reverse=True)
print("\nRanked Resumes (Resume Text, Similarity Score):")
for i, (resume, score) in enumerate(ranked_resumes, 1):
    print(f"Resume {i}: {resume}, Score: {score:.2f}")
