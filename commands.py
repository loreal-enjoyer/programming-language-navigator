import pathlib
import config


def generate_readme(path: pathlib.Path = config.LANGUAGES_LOCATION):
    print("generating readme")


def generate_language(params: list = None) -> pathlib.Path:
    def interactive() -> list[str]:
        return [input("*) Input name: "), input("*) Input description: "),
                input("*) Input website: "), input("*) Input repository: ")]

    if params == None:
        params = interactive()

    language = {s[0]: s[1] for s in list(zip(config.PARAMS_KEYS, params))}
    return _dumps(language)


def _dumps(content: dict) -> pathlib.Path:
    path = pathlib.Path(f"langs/{content["name"]}.toml")
    with path.open("w") as file:
        file.write("[language]\n")
        for k, v in content.items():
            file.write(f"{k} = {v}\n")
    return path
