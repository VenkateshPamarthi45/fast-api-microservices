install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format files
	black app/products
lint:
	#lint files
	pylint --disable=R,C *.py app
unittest:
	#test files
	python -m pytest -vv test/products_test.py

build:
	docker build -t myimage .
run:
	docker run -d --name mycontainer -p 80:8000 myimage

pre-commit: format lint unittest