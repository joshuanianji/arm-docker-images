FROM rust:1.68-slim-buster as builder

# install git
RUN apt-get update && apt-get install -y git

WORKDIR /app
RUN git clone https://github.com/typst/typst.git

WORKDIR /app/typst
RUN cargo build -p typst-cli --release

# optimized binary will be in /app/typst/target/release/typst

FROM scratch AS final 
COPY --from=builder /app/typst/target/release/typst /usr/local/bin/typst
