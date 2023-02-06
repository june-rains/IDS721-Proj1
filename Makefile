install:
	pip3 install --upgrade pip &&\
		pip3 install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C application.py

test:
	pytest test_application.py

all: install format lint test