import { useState } from "react";

const ResumeUpload = ({ onUpload }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (selectedFile) {
      onUpload(selectedFile);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6 bg-white rounded-xl shadow-md mt-6">
      <h2 className="text-xl font-bold mb-4">Upload Resume</h2>
      <input type="file" onChange={handleFileChange} className="mb-4" />
      <button
        className="px-4 py-2 bg-green-500 text-white font-semibold rounded-md hover:bg-green-600"
        onClick={handleUpload}
      >
        Upload Resume
      </button>
    </div>
  );
};

export default ResumeUpload;
