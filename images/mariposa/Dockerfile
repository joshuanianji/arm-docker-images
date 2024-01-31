FROM haskell:9.8-slim

WORKDIR /build
COPY . .

WORKDIR /build/mariposa
RUN make build
RUN mv ./mariposa /usr/local/bin/mariposa
