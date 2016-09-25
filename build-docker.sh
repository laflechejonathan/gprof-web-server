#!/bin/bash -ex

echo 'copying source code to docker directory'
mkdir -p gprof-web-server-docker/deploy/src
rsync --exclude gprof-web-server-docker . gprof-web-server-docker/deploy/src
docker build -t gprof-web-server-docker gprof-web-server-docker
