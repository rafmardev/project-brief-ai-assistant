curl -X POST "http://localhost:8000/brief" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@./app/test/test.txt" \
  -F "files=@./app/test/test2.txt"