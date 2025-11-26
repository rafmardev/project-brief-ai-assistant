python -m venv venv
pip -tr requirements.txt

curl -X POST "http://localhost:8000/upload/multiple" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@/ruta/doc1.pdf" \
  -F "files=@/ruta/doc2.jpg" \
  -F "files=@/ruta/doc3.png"

curl -X POST "http://localhost:8000/brief" \
  -H "Content-Type: multipart/form-data" \
  -F "files=./app/test/test.txt"

curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"project_id": "09b5e688-5d52-41bf-9b73-e53a25c0601b", "query": "query_example"}'

https://localhost:8000/docs