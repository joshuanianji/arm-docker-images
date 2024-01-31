FROM haskell:9.8-slim

WORKDIR /build
COPY . .

RUN make build
RUN mv ./mariposa /usr/local/bin/mariposa
