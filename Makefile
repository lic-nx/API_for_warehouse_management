
all: start migrations migrate  build run
	
	
start:
	docker-compose --env-file .env up -d

migrations:
	docker-compose --env-file .env run --rm app sh -c 'cd src && alembic revision --autogenerate -m "$(name)"'

migrate:
	docker-compose --env-file .env run --rm app sh -c 'cd src && alembic upgrade head'

build:
	docker-compose build
	
run:
	docker-compose up

downgrade:
	docker-compose --env-file .env run --rm app alembic downgrade -1

clean:
	docker stop $(docker ps -qa) 
	docker rm $(docker ps -qa)
	docker rmi -f $(docker images -qa)
	docker volume rm $(docker volume ls -q) 
	docker network rm $(docker network ls -q)