install:
	poetry install

test-task1:
	poetry run pytest tests/task1


test-task2:
	poetry run pytest tests/task2


test-task3:
	poetry run pytest tests/task3


lint:
	poetry run flake8 task1/ task2/ task3/ tests

test:
	make test-task1
	make test-task2
	make test-task3

check:
	make lint
	make test