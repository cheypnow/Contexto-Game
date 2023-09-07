up:
	docker-compose up -d --build
dev-ui:
	docker-compose up -d --build backend
	cd ./ui && npm start
down:
	docker-compose down