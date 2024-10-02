import pathlib
import config
import generation

def generate_readme(root: pathlib.Path = config.README,
                    langs_dir: pathlib.Path = config.LANGUAGES_LOCATION):
    generation.ReadmeGenerator(root, langs_dir).write_readme()


def generate_language(params: list = None) -> pathlib.Path:
    def interactive() -> list[str]:
        return [input("*) Input name: "), input("*) Input description: "),
                input("*) Input website: "), input("*) Input repository: ")]

    if params == None:
        params = interactive()

    language = generation.Language(*params)
    return _dumps(language)


def _dumps(language: generation.Language) -> pathlib.Path:
    path = pathlib.Path(f"langs/{language.name}.toml")
    with path.open("w") as file:
        for k, v in language.dict().items():
            file.write(f"{k} = \"{v}\"\n")
    return path
