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
  -d '{"project_id": "2u4panh6xjok-fb9hs47ggq3a", "query": "take some words of the files and build a phrase in english, show me english phrase and in the original language "}'

https://localhost:8000/docs