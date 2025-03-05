from pymongo import MongoClient

# Connect to MongoDB (replace with your actual URI)
client = MongoClient("mongodb://localhost:27017/")
db = client.resume_ranking

# Collections
job_descriptions = db.job_descriptions
resumes = db.resumes
