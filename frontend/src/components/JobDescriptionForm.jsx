import { useState } from "react";

const JobDescriptionForm = ({ onSubmit }) => {
  const [jobDescription, setJobDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(jobDescription);
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-xl shadow-md">
      <h2 className="text-xl font-bold mb-4">Enter Job Description</h2>
      <textarea
        className="w-full p-3 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400"
        rows="5"
        placeholder="Enter job description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />
      <button
        className="mt-4 px-4 py-2 bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600"
        onClick={handleSubmit}
      >
        Submit JD
      </button>
    </div>
  );
};

export default JobDescriptionForm;
