# automl-docker

based on rootproject/root:6.22.02-ubuntu20.04

docker and script for lea software

## Installation:

`docker build -t my-lea -f Dockerfile .`

## Usage 

`docker run --rm -it --shm-size=3.00gb -v $PWD/leasoft:/home/foo/workdir --user $(id -u) my-lea`






