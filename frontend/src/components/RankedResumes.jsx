const RankedResumes = ({ rankedCandidates, fetchRankedResumes }) => {
  const handleDeleteResume = async (resumeName) => {
    if (!window.confirm(`Are you sure you want to delete ${resumeName}?`)) return;

    try {
      const response = await fetch("http://127.0.0.1:5000/delete-resume", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: resumeName }), // Fixed key
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.error || "Failed to delete resume");
      }

      fetchRankedResumes();
    } catch (error) {
      console.error("Error deleting resume:", error.message);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-6 bg-white rounded-xl shadow-md mt-6">
      <h2 className="text-xl font-bold mb-4">Ranked Resumes</h2>
      {rankedCandidates.length === 0 ? (
        <p>No resumes ranked yet.</p>
      ) : (
        <ul>
          {rankedCandidates.map((candidate, index) => (
            <li key={index} className="flex justify-between items-center py-2 border-b">
              <span>{candidate.name} - {candidate.score}% match</span>
              <button 
                className="px-2 py-1 bg-red-500 text-white rounded-md hover:bg-red-600"
                onClick={() => handleDeleteResume(candidate.name)}
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default RankedResumes;
