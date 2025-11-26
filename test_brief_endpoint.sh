curl -X POST "http://localhost:8000/brief" \
  -H "Content-Type: multipart/form-data" \
  -F "files=@./test/test.txt" \
  -F "files=@./test/test2.txt"