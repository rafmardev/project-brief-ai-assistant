# FastAPI Document Summarization & Query API

A backend service built with **FastAPI** that allows users to upload documents and get summaries, as well as perform queries on previously uploaded content.

The project follows a Clean Architecture approach, aiming to decouple the different layers of the application and promote maintainability, testability, and scalability. The architecture separates responsibilities into distinct layers, ensuring that business logic is independent from frameworks, databases, or external services.
**Core Principles**
- Separation of Concerns: Each layer has a clear responsibility.
- Dependency Rule: Inner layers (use cases, entities) do not depend on outer layers (frameworks, APIs, DB).
- Testability: Business logic can be tested independently from FastAPI or storage layers.
- Extensibility: New use cases, endpoints, or storage backends can be added with minimal impact on existing code.

**Use Case 1: File Upload & Store Creation**
1. Upload Endpoint - API Layer (`/brief`)
- Receives one or multiple documents from the user.
- Receives HTTP requests, validates input, and delegates to the use case.
- Calls the File Upload Use Case.
- Returns a response with the generated store_id and a summary.
2. Use Case Logic
- Creates a new store to organize uploaded files.
Uploads files to the store (e.g., Gemini File Store or server storage).
- Persists documents locally with the associated store_id.
3. Repository
- Saves a file in the folder created with its store_id.
4. Gemini Integration Services
- Uploads a file, creates stores.

**Use Case 2: Semantic Query**
1. Query Endpoint (`/query`)
- Receives a query in English and a store_id referencing a previously uploaded project.
- Returns an answer or relevant snippet to the user.

2. Use Case Logic
- Loads the relevant documents from the store.
- Executes a semantic search or natural language query over the content.
- Returns an answer or relevant snippet to the user.

3. Gemini Integration Service
- Makes sematic queries to Gemini API. 

---

## Table of Contents

- [Features](#features)
- [Endpoints](#endpoints)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)

---

## Features

- Upload multiple documents and generate a concise summary.
- Query previously uploaded documents in English.
- Fast and lightweight API built on FastAPI.
- Easily extensible for additional endpoints.

---

## Endpoints

### 1. `/brief` – Upload & Summarize Documents

**Method:** `POST`  
**Description:** Upload one or multiple documents. The API returns a summarized version of the uploaded content.

**Request Example (multipart/form-data):**
```http
POST /brief
Content-Type: multipart/form-data

files[]: file1.pdf
files[]: file2.docx
```

**Response**
```json
{"project_id":"2u4panh6xjok-fb9hs47ggq3a","brief":"The files in the store, `test.txt` and `test2.txt`, both contain \"Lorem ipsum\" placeholder text. This text is a standard filler used to demonstrate the visual form of a document or a typeface without relying on meaningful content. It describes a scenario where one feels pain and then seeks to alleviate or escape it, but the specific details are not relevant as it's a placeholder."}
```

### 2. query – Query Uploaded Project Documents
Method: POST
Description: Submit a query in English to search or retrieve information from the previously uploaded documents.
**Request Example (JSON):**
```json
{"project_id": "2u4panh6xjok-fb9hs47ggq3a", "query": "take some words of the files and build a phrase in english, show me english phrase and in the original language "}
```
**Response**
```json
{"results":[{"file":"test2.txt","snippet":{"message":"Based on the content of the files, which contain \"Lorem ipsum\" text, the original language is Latin.\n\nHere's a phrase built from words found in the files:\n\nOriginal Latin phrase: \"Dolor sit amet\"\nEnglish phrase: \"Pain itself\"","success":true}},{"file":"test.txt","snippet":{"message":"The files provided contain \"Lorem ipsum\" placeholder text. As a result, I cannot extract meaningful words to construct a coherent phrase.","success":true}}]}%    
```

---

## Installation
```bash
python -m venv venv
# Linux and Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```
In config folder, create .env file and update your GEMINI_API_KEY following .env.example file.

``` bash
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

---

## Usage

You can access the SwaggerUI documentation of the API once the server is deployed locally in:

https://localhost:8000/docs

For test purposes, you can use these examples or execute bashes scripts in app folder:

curl -X POST "http://localhost:8000/brief" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@./app/test/test.txt" \
  -F "files=@./app/test/test2.txt"

curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"project_id": "2u4panh6xjok-fb9hs47ggq3a", "query": "take some words of the files and build a phrase in english, show me english phrase and in the original language "}'

---

## Requirements
Python 3.10+

## Future Improvements
Potential enhancements to the system include:
1. **Observability Layer**
- Metrics Collection: Track request latency, throughput, error rates, and file upload times.
- Distributed Tracing: Trace requests across different components (FastAPI, file store) to identify slow points.
- Logging Enhancements: Structured and centralized logging to monitor errors, warnings, and business events.
- Alerts & Dashboards: Integration with tools like Prometheus, Grafana to visualize metrics and set up alerts.
**Benefits:**
- Early detection of bottlenecks in file uploads or semantic queries.
- Better understanding of system performance under load.
- Improved maintainability and faster debugging in production.
2. **Event-Driven Programming for Parallel Operations**
- Implement asynchronous or event-driven workflows to handle operations concurrently, such as:
  - Uploading multiple files simultaneously.
  - Persisting files and metadata in the system in parallel.
- This could be achieved using message brokers like Kafka.
**Benefits:**
- Reduced latency for bulk file uploads.
- More efficient use of system resources.
- Scalable architecture that can handle high volumes of concurrent operations.

## Future Production Deployment
For deploying the FastAPI backend to production, a cloud-based approach is recommended to ensure scalability, reliability, and maintainability. Some best practices and considerations include:
1. **Cloud Infrastructure Options**
- Containers (PaaS / Orchestrated): Docker + Kubernetes (EKS, GKE, AKS)
  - Easy scaling and reproducible deployments.
  - Supports rolling updates and zero-downtime deployments.
- Serverless Functions: AWS Lambda, Google Cloud Functions
  - Pay-per-use; ideal for short-lived tasks such as semantic queries or file processing.
  - No need to maintain a server, but may require adaptation for large file uploads.
- Infrastructure as Code (IaC) with Terraform
- Instead of manually provisioning cloud resources, consider using Terraform to define your infrastructure as code.
2. **Deployment Best Practices**
- Save operations metadata with Gemini API in a database.
- Environment Configuration: Separate environment variables for production (API keys, database URLs).
- Security: Enable HTTPS, secure storage for files, and proper authentication/authorization.
- Scalability: Use auto-scaling for handling variable loads and high concurrency.
- Persistent Storage: Use cloud object storage (S3, GCS, Azure Blob) for uploaded documents.
3. **CI/CD Integration**
- Automate deployments using GitHub Actions, GitLab CI/CD, or cloud-native pipelines.
- Include automated tests and linting before deployment.
- Ensure rollback strategies in case of failed deployments.
