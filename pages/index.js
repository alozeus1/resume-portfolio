import { useEffect, useState } from "react";

export default function Home() {
  const [resume, setResume] = useState("");

  useEffect(() => {
    fetch("/resume.json")
      .then((res) => res.json())
      .then((data) => setResume(JSON.stringify(data, null, 2)));
  }, []);

  return (
    <div>
      <h1>My Resume</h1>
      <pre>{resume}</pre>
      <a href="YOUR_LAMBDA_PDF_URL" download>Download Resume as PDF</a>
    </div>
  );
}