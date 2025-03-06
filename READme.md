# Dynamic Resume Project

## Setup Instructions

### Deploy Backend
1. Deploy `lambda_generate_pdf` to AWS Lambda.
2. Deploy `lambda_upload_files` to AWS Lambda.
3. Set environment variables (`RESUME_URL`, `S3_BUCKET_NAME`).

### Deploy Frontend
1. Deploy Next.js app on Vercel.
2. Update `YOUR_LAMBDA_PDF_URL` in `index.js`.

### Automate Updates
- GitHub Actions auto-generates PDFs when resume changes.

### API Endpoints
- `POST /upload` → Upload files to S3
- `GET /pdf` → Generate and download resume PDF