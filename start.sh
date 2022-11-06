docker-compose up -d --build
curl http://localhost:8081/api/start &
docker-compose logs -f