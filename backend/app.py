from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import database
import ml_model

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store Job Description
@app.route("/submit-jd", methods=["POST"])
def submit_job_description():
    data = request.json
    job_description = data.get("jobDescription")

    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    database.job_descriptions.insert_one({"description": job_description})
    return jsonify({"message": "Job description saved successfully"}), 201

# Upload Resume
@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract text from resume
    extracted_text = ml_model.extract_text_from_pdf(file_path)

    # Store in MongoDB
    database.resumes.insert_one({"name": file.filename, "text": extracted_text})

    return jsonify({"message": "Resume uploaded successfully"}), 201

# Rank Resumes
@app.route("/rank-resumes", methods=["GET"])
def rank_resumes():
    latest_jd = database.job_descriptions.find_one({}, sort=[("_id", -1)])

    if not latest_jd:
        return jsonify({"error": "No job description found"}), 400

    resumes = list(database.resumes.find({}, {"_id": 0, "name": 1, "text": 1}))
    ranked_resumes = ml_model.rank_resumes(latest_jd["description"], resumes)

    return jsonify({"rankedCandidates": ranked_resumes})

# Delete Resume API
@app.route("/delete-resume", methods=["POST"])
def delete_resume():
    data = request.json
    resume_name = data.get("name")  # Fixed the key name

    if not resume_name:
        return jsonify({"error": "Resume name is required"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, resume_name)
    if os.path.exists(file_path):
        os.remove(file_path)

    result = database.resumes.delete_one({"name": resume_name})

    if result.deleted_count == 0:
        return jsonify({"error": "Resume not found in database"}), 404

    return jsonify({"message": "Resume deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
