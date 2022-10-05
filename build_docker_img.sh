export $(grep -v '^#' EDIT.env | xargs)
docker build -t ${NAME}:minimal .
docker-compose up -d
