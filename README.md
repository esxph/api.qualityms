# api.qualityms

# To build run
docker-compose up --build -d

# Start migration
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Deletes all containers and everything
docker-compose down -v