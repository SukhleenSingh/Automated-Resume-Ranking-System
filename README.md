# AI/ML-Based Automated Resume Ranking System

## 📌 Overview
This project is an **AI/ML-powered Automated Resume Ranking System** that helps recruiters rank resumes based on job descriptions. It extracts text from uploaded resumes, compares them with a given job description, and ranks them based on relevance.

## 🚀 Features
- Upload resumes in **PDF format**
- Extract text from resumes
- Store resumes and job descriptions in **MongoDB**
- Rank resumes based on **job relevance**
- Delete resumes from both **frontend & backend**

## 🛠 Tech Stack
- **Frontend:** React (Vite), TailwindCSS
- **Backend:** Flask (Python)
- **Database:** MongoDB
- **ML Processing:** Natural Language Processing (NLP) using `spaCy` & `TF-IDF`

---

## 🏗 Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SukhleenSingh/Automated-Resume-Ranking-System
cd ai-resume-ranking
```

### 2️⃣ Backend Setup (Flask API)
#### Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### Run the Flask Server
```bash
python app.py
```
The server will start on `http://127.0.0.1:5000`

---

### 3️⃣ Frontend Setup (React Vite)
#### Install Dependencies
```bash
cd frontend
npm install
```

#### Run the React App
```bash
npm run dev
```
Frontend will start at `http://localhost:5173`

---

## 📂 Project Structure
```
📦 ai-resume-ranking
 ┣ 📂 backend
 ┃ ┣ 📜 app.py                # Flask backend
 ┃ ┣ 📜 database.py           # MongoDB connection
 ┃ ┣ 📜 ml_model.py           # ML Ranking Logic
 ┃ ┣ 📂 uploads               # Stored Resumes
 ┃ ┗ 📜 requirements.txt      # Backend Dependencies
 ┣ 📂 frontend
 ┃ ┣ 📂 src
 ┃ ┃ ┣ 📜 App.jsx             # Main React Component
 ┃ ┃ ┣ 📜 RankedResumes.jsx   # Ranks & Deletes Resumes
 ┃ ┃ ┗ 📜 UploadForm.jsx      # Upload Resume & Job Description
 ┃ ┣ 📜 index.js              # React Entry Point
 ┃ ┗ 📜 package.json          # Frontend Dependencies
 ┗ 📜 README.md
```

