FROM golang:1.18-bullseye

# install git
WORKDIR /
RUN apt-get update && apt-get install -y git make
RUN git clone --depth 1 https://github.com/bcicen/ctop.git 

WORKDIR /ctop 
RUN go mod download 
RUN make build
RUN mkdir -p /go/bin
RUN mv -v ctop /go/bin/

# https://github.com/bcicen/ctop/blob/master/Dockerfile
FROM scratch
ENV TERM=linux
COPY --from=0 /go/bin/ctop /ctop
ENTRYPOINT ["/ctop"]