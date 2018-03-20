all:
	$(MAKE) build
	$(MAKE) run

build:
	docker build . -t plank
	# TODO find a real location to stick this
	mkdir -p /tmp/data/content/img/
	chcon -Rt svirt_sandbox_file_t /tmp/data

run:
	# if python image
	#docker run --rm --name plank -p 4000:5000 -v "/tmp/data:/app/app/data" plank
	# uwsgi-nginx-flask image
	docker run --rm --name plank -p 4000:80 -v "/tmp/data:/app/app/data" plank

daemon:
	# if python image
	#docker run --rm -d --name plank -p 4000:5000 -v "/tmp/data:/app/app/data" plank
	# uwsgi-nginx-flask image
	docker run --rm -d --name plank -p 4000:80 -v "/tmp/data:/app/app/data" plank

