# Arm Docker Images

Support for native arm-based Docker images remains a bit spotty, especially since Mac M1 runners on Github Actions costs money. This repo holds a collection of docker images built for ARM64, with help from my [Oracle Free-tier VM](https://www.oracle.com/ca-en/cloud/free/)

## Available Images

- [ctop](./images/ctop/) - Top-like interface for container metrics
- [mariposa](./images/mariposa/) - Toy language with time travel
- [purescript-spago](./images/purescript-spago/) - Purescript and Spago (Warning: might be old)
- [aria2c-with-webui](./images/aria2c-with-webui) - Aria2 with a frontend, based off of [abcminiuser/docker-aria2-with-webui](https://github.com/abcminiuser/docker-aria2-with-webui)
- [docker-postgres-upgrade](./images/docker-postgres-upgrade) - `pg_upgrade` in a Docker container

## Making a new image 

```bash
python scripts/new.py
```

## Success Stories

- [Typst](https://github.com/typst/typst) - the Typst devcontainer feature supports ARM now: see [michidk/devcontainers-features#5](https://github.com/michidk/devcontainers-features/pull/5)

## Deprecated Images

Images that I don't care about anymore

- [Docker X11 Bridge](./archive/docker-x11-bridge)
- [Julia Devcontainer](./archive/julia-devcontainer/)
- [Llama CPP](./archive/llama-cpp/)
