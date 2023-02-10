# DnD Character Sheet Service

## Running the service
First create a .env file with the following content:
```
COMPOSE_FILE=docker-compose.yml:docker-compose.dev.yml
```

Then run the following command:
```bash
docker-compose up --build
```