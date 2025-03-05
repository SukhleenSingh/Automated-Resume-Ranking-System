import { useState, useEffect } from "react";
import JobDescriptionForm from "../components/JobDescriptionForm";
import ResumeUpload from "../components/ResumeUpload";
import RankedResumes from "../components/RankedResumes";

const Home = () => {
  const [rankedCandidates, setRankedCandidates] = useState([]);

  const fetchRankedResumes = async () => {
    const response = await fetch("http://127.0.0.1:5000/rank-resumes");
    const data = await response.json();
    if (data.rankedCandidates) {
      setRankedCandidates(data.rankedCandidates);
    }
  };

  const handleSubmitJD = async (jobDescription) => {
    await fetch("http://127.0.0.1:5000/submit-jd", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ jobDescription }),
    });

    fetchRankedResumes();
  };

  const handleUploadResume = async (file) => {
    const formData = new FormData();
    formData.append("resume", file);

    await fetch("http://127.0.0.1:5000/upload-resume", {
      method: "POST",
      body: formData,
    });

    fetchRankedResumes();
  };

  return (
    <div className="min-h-screen bg-black p-6">
      <h1 className="text-3xl font-bold text-center mb-6">
        Automated Resume Ranking System
      </h1>
      <JobDescriptionForm onSubmit={handleSubmitJD} />
      <ResumeUpload onUpload={handleUploadResume} />
      <RankedResumes rankedCandidates={rankedCandidates} fetchRankedResumes={fetchRankedResumes} />
    </div>
  );
};

export default Home;
