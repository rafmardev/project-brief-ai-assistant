python -m venv venv
pip -tr requirements.txt

curl -X POST "http://localhost:8000/upload/multiple" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@/ruta/doc1.pdf" \
  -F "files=@/ruta/doc2.jpg" \
  -F "files=@/ruta/doc3.png"

curl -X POST "http://localhost:8000/brief" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@./app/test/test.txt" \
  -F "files=@./app/test/test2.txt"

curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"project_id": "99b08fbc-6863-4f37-a36d-8e0725b0fcda", "query": "query_example"}'

https://localhost:8000/docs