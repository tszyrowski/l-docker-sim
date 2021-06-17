# Workshop for Python Docker

Starting point:  
https://www.youtube.com/watch?v=OkidaZmnADw

# docker build:

The application should run in a container. To build:

```shell
cd <project_path>/l-docker-sim
docker build -t docker-sim app/
docker run --rm docker-sim
```

The application will require database. To achieve it, the `compose` file was added.
To run:
```shell
docker-compose up
```