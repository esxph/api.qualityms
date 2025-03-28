# api.qualityms

# To build run
docker-compose up --build -d

# Deletes all containers and everything (incluiding the volumes)
docker-compose down -v


# To safely upgrade the containers without erasing data from the volumes
docker compose down --remove-orphans
docker compose up --build -d
