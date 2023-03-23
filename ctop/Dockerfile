FROM debian:11-slim

# install git
RUN apt-get update && apt-get install -y git
RUN git clone --depth 1 https://github.com/bcicen/ctop.git 

WORKDIR /ctop 
RUN make build 
