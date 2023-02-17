# This Dockerfile builds a container for CMPUT 267 devcontainer

ARG VARIANT=3.10-bullseye
FROM mcr.microsoft.com/vscode/devcontainers/python:${VARIANT}

# install latex
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends texlive-full latexmk perl

# configure latexindent
# https://newptcai.gitlab.io/blog/latexindent/
RUN yes | sudo cpan -i App::cpanminus \
    && sudo cpanm YAML::Tiny \
    && sudo cpanm File::HomeDir \
    && sudo cpanm Unicode::GCString \
    && sudo cpanm Log::Log4perl \
    && sudo cpanm Log::Dispatch::File

# install julia by JILL.py
ENV PATH="${PATH}:/root/.local/bin"
RUN export DEBIAN_FRONTEND=noninteractive \
    && pip install jill --user -U \
    && jill install 1.8 --confirm

# install Pluto@0.19 via Julia
# https://discourse.julialang.org/t/how-to-install-a-specific-version-of-a-package-with-pkg-add/29242/9
RUN julia -e "import Pkg; Pkg.add(name=\"Pluto\", version=\"0.19\")"