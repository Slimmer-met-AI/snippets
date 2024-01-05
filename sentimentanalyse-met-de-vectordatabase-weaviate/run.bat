@echo off

docker run -p 8080:8080 --env-file vars.env -v "G:/My Drive/SlimmermetAI/Website/backend/weaviate/data":/var/lib/weaviate -d weaviate-database

pause