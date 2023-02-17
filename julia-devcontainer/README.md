# Julia Devcontainer

The current official devcontainer for the Julia language [does not support ARM-based machines](https://github.com/julia-vscode/julia-devcontainer/blob/master/.github/workflows/docker-publish.yml).

For my intro to ML class, I would rather have a self contained environment to use in my M1 mac. It has quite a few dependencies, so I decided to create a devcontainer for it.

## Contents

- Julia 1.8 (installed by [jill.py](https://github.com/joshuanianji/cmput267/blob/main/.devcontainer/Dockerfile))
- Python 3.10
- Latex + latexindent (uses latex full!)
- Pluto 0.19
