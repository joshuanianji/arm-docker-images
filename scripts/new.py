# create a docker image spec

import os


def main():
    unparsed_name = input("Name: ")

    # make sure name has no spaces
    name = unparsed_name.replace(" ", "-")
    if name != unparsed_name:
        print(f"Name: {name}")

    # run `mkdir name`
    os.system(f"mkdir images/{name}")
    os.system(f"touch images/{name}/Dockerfile")
    os.system(f"touch images/{name}/README.md")
    os.system(f"echo '# {name}' >> images/{name}/README.md")
    os.system(f"touch .github/workflows/{name}.yml")

    with open(f"./scripts/template.yml", "r") as f:
        template = f.read()
        new_template = template.replace("$NAME", name)
        with open(f"./.github/workflows/{name}.yml", "w") as f:
            f.write(new_template)


if __name__ == "__main__":
    main()
