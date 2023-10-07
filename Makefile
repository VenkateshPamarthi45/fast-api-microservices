install:
	#install commands
	pip install -r requirements.txt
format:
	#format files
	black app/products
lint:
	#lint files
build:
	docker build -t myimage .
run:
	docker run -d --name mycontainer -p 80:8000 myimage