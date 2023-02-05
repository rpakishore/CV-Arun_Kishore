export $(grep -v '^#' EDIT.env | xargs)
id=$(docker ps -aqf "name=${NAME}")

docker container stop $id 2>/dev/null
docker container rm $id 2>/dev/null

docker build -t ${NAME}:latest .
docker-compose -f docker-compose-alexhost.yml up -d
