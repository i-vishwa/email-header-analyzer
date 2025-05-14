# Email Header Analyzer - Minor Project

A Python + Gradio tool for analyzing raw email headers.  
Detects spoofing, extracts IPs, and parses sender information.

🔗 **Live Demo**: [Click here](https://email-header-analyzer-11779385448.asia-south1.run.app/)

## Features
- Extracts `From`, `To`, `Subject`, and `Return-Path`
- Parses all relay IPs from `Received` headers
- Detects possible email spoofing
- Simple Gradio interface

## Tech Stack
- Backend: Python
- UI: Gradio
- Cloud: Google Cloud Run
- Containerized with Docker

## How to Deploy
1. Install [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
2. Run:
```bash
gcloud init
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/email-header-analyzer
gcloud run deploy ...
