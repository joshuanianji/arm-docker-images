FROM haskell:9.2.5

RUN git clone https://github.com/avh4/elm-format
WORKDIR /elm-format

# Build elm-format
RUN ./dev/build.sh -- build

# The final binary will be ./_build/elm-format
