python -m venv venv
pip -tr requirements.txt

curl -X POST "http://localhost:8000/upload/multiple" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@/ruta/doc1.pdf" \
  -F "files=@/ruta/doc2.jpg" \
  -F "files=@/ruta/doc3.png"

curl -X POST "http://localhost:8000/brief" \
  -H "Content-Type: multipart/form-data" \
  -F "files=./app/test/test.txt" \

https://localhost:8000/docs