# llama-cpp

[Llama.cpp](https://github.com/ggerganov/llama.cpp) Docker images built for ARM based machines.

## Usage

[More info](https://github.com/ggerganov/llama.cpp#docker)

Suppose you have your models in `/llama/models` and you want to generate 512 tokens using the (quantized) `ggml-model-q4_0.bin` model.

```bash
docker run -v /llama/models:/models ghcr.io/joshuanianji/arm-docker-images/llama.cpp:light -m /models/7B/ggml-model-q4_0.bin -p "Building a website can be done in 10 simple steps:" -n 512
```