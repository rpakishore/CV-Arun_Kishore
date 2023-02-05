export $(grep -v '^#' EDIT.env | xargs)
docker build -t ${NAME}:latest .
docker-compose -f docker-compose-local.yml up -d
