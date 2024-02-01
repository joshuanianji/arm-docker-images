# Mariposa

Docker images for the [Mariposa Language](https://github.com/ambulancja/mariposa), a python-inspired language with time-travelling.

Mariposa binary is in `/usr/local/bin/mariposa`.

## Running a Mariposa File

Mariposa currently does not support reading files through stdin, so you'd have to use a Docker mount to evaluate code in the container.

Suppose you had a test file `program.m` in your current directory. You can run the following:

```bash
docker run -v "$(pwd)":/files ghcr.io/joshuanianji/arm-docker-images/mariposa:latest /files/program.m
```
