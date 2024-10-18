# Automated-Resume-Ranking-System
Code Breakdown:
1. NLP Preprocessing:
   Uses Spacy to preprocess both job descriptions and resumes (tokenization, lemmatization, removing stopwords).
2. Vectorization and Similarity Calculation:
   Uses TF-IDF Vectorizer to convert resumes and job descriptions into vectors.
   Calculates cosine similarity between the job description and each resume.
3. Machine Learning (RandomForest Regressor):
   Trains a RandomForestRegressor to predict relevance scores based on the similarity features (for training purposes, relevance scores are assumed).
4. AIOps Monitoring:
   Simulates system response times and uses IsolationForest to detect performance anomalies.
5. LLMOps Feedback (Optional):
   Uses a pre-trained transformer (Hugging Face’s pipeline) to provide personalized feedback on how resumes can be improved based on the job description.
6. Final Resume Ranking:
   Sorts and prints the resumes based on their similarity scores to the job description
