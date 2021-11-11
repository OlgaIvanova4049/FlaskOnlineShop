app_name?=backend-shop
root_path?=app
message?=migration message
version?=head

migration:
	docker exec -it $(app_name) sh -c "alembic  revision --autogenerate -m \"$(message)\""

migrate:
	docker exec -it $(app_name) sh -c "alembic  -x data=$(with_data) upgrade $(version)"

downgrade:
	docker exec -it $(app_name) sh -c "alembic  downgrade $(version)"
