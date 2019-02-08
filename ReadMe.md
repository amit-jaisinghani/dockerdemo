# Hello World
`docker run hello-world`

Run ubuntu container, and attach to local command-line session, and runs /bin/bash

`docker run -it ubuntu /bin/bash`

# Type of networking
## Bridge (default)
```bash
docker run -d --name nginx-3 -p 10000:80 nginx
docker run -d --name nginx-4 -p 10001:80 nginx
```

### Can create your own bridge
```bash
docker network create --subnet=172.18.0.0/16 mynet123
docker run -d --name nginx-3 --net=mynet123 -p 10000:80 nginx
```

## Host (use the host's networking stack)
`docker run -d --name nginx-1 --net=host nginx`

## Overlay (across multiple hosts)
k8s, cni, etc

# Useful commands
```bash
docker ps
docker image ls
docker ps -a
docker kill <containerName>
```

# Applications
Write dockerfile and build

`docker build --tag=friendlyhello .`

Run in foreground

`docker run -p 4000:80 friendlyhello`

Run as background

```
docker run -d -p 4000:80 friendlyhello

docker container ls
docker container stop <ID>
```

# I/O

```bash
cat app.py

docker run -d demo/appfile
docker exec -it <name> /bin/bash
```

# Mount a volume to /test

`docker run -v /home/brat/Learning/demo/appFile:/test -d demo/appfile`
