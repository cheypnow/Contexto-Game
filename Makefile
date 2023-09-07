up:
	docker-compose up -d --build
dev-ui:
	docker-compose up -d backend
	cd ./ui && npm start
down:
	docker-compose down