import json
import requests
import os
from weasyprint import HTML

def lambda_handler(event, context):
    resume_url = os.getenv("RESUME_URL", "https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/resume-portfolio/main/frontend/public/resume.json")
    
    try:
        response = requests.get(resume_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
    
    html_content = f"""
    <html><body><pre>{json.dumps(response.json(), indent=4)}</pre></body></html>
    """
    
    pdf_file = "/tmp/resume.pdf"
    HTML(string=html_content).write_pdf(pdf_file)
    
    with open(pdf_file, "rb") as f:
        pdf_encoded = f.read()
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/pdf",
            "Content-Disposition": "attachment; filename=resume.pdf"
        },
        "body": pdf_encoded,
        "isBase64Encoded": True
    }