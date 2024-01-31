# ctop

See: [ctop](https://github.com/bcicen/ctop)

## Usage

```bash
docker run --rm -ti --name=ctop --volume /var/run/docker.sock:/var/run/docker.sock:ro ghcr.io/joshuanianji/arm-docker-images/ctop:latest
```

Or, you can set an alias

```.bashrc
alias dockertop='docker run --rm -ti --name=ctop --volume /var/run/docker.sock:/var/run/docker.sock:ro ghcr.io/joshuanianji/arm-docker-images/ctop:latest'
```