install:
	#install commands
format:
	#format files
	black *.py products
lint:
	#lint files
build:
	docker build -t myimage .
run:
	docker run -d --name mycontainer -p 80:8000 myimage