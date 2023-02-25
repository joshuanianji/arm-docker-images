# ARM Support for Elm-format

Building elm-format by following [#723](https://github.com/avh4/elm-format/issues/723) while I wait for official support.

This image will be useful to import the `elm-format` binary into other images.

## Usage

```dockerfile
FROM ghcr.io/joshuanianji/arm-docker-images/elm-format-arm:latest AS elm-format-binary

FROM base-image

COPY --from=elm-format-binary /dist/elm-format /usr/local/bin/elm-format
```
