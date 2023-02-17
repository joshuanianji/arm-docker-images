# Arm Docker Images

Support for native arm-based Docker images remains a bit spotty, especially since Github actions only support x86_64 runners ([Maybe this will change soon?](https://github.com/github/roadmap/issues/528) 👀). Oftentimes, especially for compiling software, qemu emulation is too slow to be usable.

This repository contains ARM-Based Docker images for some languages and software, mainly for personal use. I build the arm images via [Buildx Remote Builders](https://www.docker.com/blog/speed-up-building-with-docker-buildx-and-graviton2-ec2/#), connected to my [Oracle Free-tier VM](https://www.oracle.com/ca-en/cloud/free/).
