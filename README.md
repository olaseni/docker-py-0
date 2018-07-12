# docker-py-0
An initiation to docker build

$ `docker image rm --force tripodwire/flask-0:latest`
$ `docker build -t tripodwire/flask-0 .`
$ `docker run --rm -p 9000:5000 tripodwire/flask-0`
