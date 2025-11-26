# FastAPI Document Summarization & Query API

A backend service built with **FastAPI** that allows users to upload documents and get summaries, as well as perform queries on previously uploaded content.

The project follows a Clean Architecture approach, aiming to decouple the different layers of the application and promote maintainability, testability, and scalability. The architecture separates responsibilities into distinct layers, ensuring that business logic is independent from frameworks, databases, or external services.
**Core Principles**
- Separation of Concerns: Each layer has a clear responsibility.
- Dependency Rule: Inner layers (use cases, entities) do not depend on outer layers (frameworks, APIs, DB).
- Testability: Business logic can be tested independently from FastAPI or storage layers.
- Extensibility: New use cases, endpoints, or storage backends can be added with minimal impact on existing code.
**Use Case 1: File Upload & Store Creation**
1. Upload Endpoint (`/brief`)
- Receives one or multiple documents from the user.
- Calls the File Upload Use Case.
2. Use Case Logic
- Creates a new store to organize uploaded files.
Uploads files to the store (e.g., Gemini File Store or server storage).
- Persists metadata locally (or in a database) with the associated store_id.
3. API Layer
- Receives HTTP requests, validates input, and delegates to the use case.
- Returns a response with the generated store_id or a summary.

**Use Case 2: Semantic Query**
1. Query Endpoint (/query)
- Receives a query in English and a store_id referencing a previously uploaded project.
2. Use Case Logic
- Loads the relevant documents from the store.
- Executes a semantic search or natural language query over the content.
- Returns an answer or relevant snippet to the user.
3. API Layer
- Receives the HTTP request, validates parameters, and delegates to the query use case.
- Formats and returns the response to the client.

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
- Easily extensible for additional endpoints or NLP features.

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
pip -tr requirements.txt
```
---

## Usage

You can access the SwaggerUI documentation of the API once the server is deployed locally in:

https://localhost:8000/docs

For test purposes, you can use these examples

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
- Distributed Tracing: Trace requests across different components (FastAPI, file store, NLP services) to identify slow points.
- Logging Enhancements: Structured and centralized logging to monitor errors, warnings, and business events.
- Alerts & Dashboards: Integration with tools like Prometheus, Grafana, or Elastic Stack to visualize metrics and set up alerts.
**Benefits:**
- Early detection of bottlenecks in file uploads or semantic queries.
- Better understanding of system performance under load.
- Improved maintainability and faster debugging in production.
2. Event-Driven Programming for Parallel Operations
- Implement asynchronous or event-driven workflows to handle operations concurrently, such as:
  - Uploading multiple files simultaneously.
  - Persisting files and metadata in the system in parallel.
- This could be achieved using async/await in FastAPI, Celery workers, or message brokers like RabbitMQ or Kafka.
**Benefits:**
- Reduced latency for bulk file uploads.
- More efficient use of system resources.
- Scalable architecture that can handle high volumes of concurrent operations.