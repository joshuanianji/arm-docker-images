# Purescript 0.15.7 uses GHC 9.2.4 - but I think stack installs ghc itself...
ARG GHC_VERSION="9.2.4"
# stack, on the other hand, uses LTS-18.24 ~ GHC 8.10.7
# https://github.com/purescript/spago/blob/master/stack.yaml
ARG GHC_VERSION_STACK="8.10.7"

# ========================== #
# Build purescript from source
FROM haskell:${GHC_VERSION} as purs-builder
ARG PURESCRIPT_VERSION="0.15.7"

WORKDIR /root

# Install stack, if the architecture is not amd64
RUN if [ "$(uname -m)" != "x86_64" ]; then curl -sSL https://get.haskellstack.org/ | sh; \
    else stack setup; fi

# Compile purescript from source
RUN stack update && stack unpack purescript-${PURESCRIPT_VERSION}
WORKDIR /root/purescript-${PURESCRIPT_VERSION}
RUN stack install --flag purescript:RELEASE
ENV PATH="/root/.local/bin:${PATH}"


# ========================== #
# Build spago from source
FROM haskell:${GHC_VERSION_STACK} as spago-builder
ARG SPAGO_VERSION="0.20.9"

# install stack if the architecture is not amd64
# else, run stack setup
RUN if [ "$(uname -m)" != "x86_64" ]; then curl -sSL https://get.haskellstack.org/ | sh; \
    else stack setup; fi

# spago requires LLVM and libnuma i think
RUN apt-get update && apt-get install -y \
    libnuma-dev llvm-11 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root
RUN git clone --depth 1 -b ${SPAGO_VERSION} https://github.com/purescript/spago.git
WORKDIR /root/spago
RUN make install

# ========================== #
# Retrieve binaries
FROM mcr.microsoft.com/devcontainers/javascript-node:16

# copy purescript binary and spago from builder
COPY --from=purs-builder /root/.local/bin/purs /usr/local/bin/purs
COPY --from=spago-builder /root/.local/bin/spago /usr/local/bin/spago

# now, purescript and spago are installed!