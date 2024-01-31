# Arm Docker Images

Support for native arm-based Docker images remains a bit spotty, especially since Mac M1 runners on Github Actions costs money

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
