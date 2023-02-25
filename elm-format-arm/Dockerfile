FROM haskell:9.2.5 AS build

RUN git clone https://github.com/avh4/elm-format
WORKDIR /elm-format

# Build elm-format
# https://github.com/avh4/elm-format/blob/6accab625f3077eb61274d0adeb3b9abf4d0ffa9/.github/workflows/CI.yml
RUN cabal v2-update
RUN ./dev/build.sh -- dependencies
RUN ./dev/build.sh -- build

# The final binary will be ./_build/elm-format
FROM scratch 
COPY --from=build /elm-format/_build/elm-format /dist/elm-format
