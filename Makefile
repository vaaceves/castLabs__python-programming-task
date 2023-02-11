# Makefile

#
build:
	docker-compose build

#
run:
	docker-compose up

#
test:
	# docker-compose run proxy python tests.py
	docker-compose run proxy pytest -vv

#
.PHONY: build run test