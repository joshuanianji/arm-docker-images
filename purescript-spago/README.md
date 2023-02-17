# Purescript & Spago

Purescript prebuild binaries [only contains `x86-64`](https://github.com/purescript/purescript/blob/master/INSTALL.md#official-prebuilt-binaries) versions, so to get an arm-based version, you need to build it yourself.

Similarly, `spago`, the purescript package manager, is not available for arm-based architectures. Installing it via `npm` will fail with the following:

```bash
qemu-x86_64: Could not open '/lib64/ld-linux-x86-64.so.2': No such file or directory
```

## Using this image

You can either:

1. Extract the binary from the image and use it in your own image`
2. Use this image as a base image

TODO: add example once GH Action deployments are done
