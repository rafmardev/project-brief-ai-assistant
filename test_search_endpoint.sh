# the project_id or store_id is available in the response of the /brief endpoint or in the infrastructure/storage folder, as every folder is named with the project_id/store_id
curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"project_id": "USE-A-PROJECT_ID(STORE_ID)-VALID", "query": "take some words of the files and build a phrase in english, show me english phrase and in the original language "}'