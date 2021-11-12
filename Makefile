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

test:
	python3 -m pytest --cov-config=.coveragerc --cov=app

mypy:
	python -m mypy .

flake8:
	python -m flake8

black:
	python -m black -l 79 .

