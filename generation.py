import pathlib
import tomllib
from dataclasses import dataclass, asdict


@dataclass
class Language:
    name: str
    description: str
    website: str
    repository: str

    dict = asdict


@dataclass
class Format:
    language_format: str = (
            "### {name}\n"
            "{description}\n\n"
            "---\n\n"
            "* [Official Website: {website}]({website})\n"
            "* [Repository: {repository}]({repository})"
            )
    separation_format: str = "\n\n"


class ReadmeGenerator:
    def __init__(self, readme: pathlib.Path,
                 langs_dir: pathlib.Path,
                 formatting: Format = Format()):
        self.readme = readme
        self.langs_dir = langs_dir
        self.formatting = formatting

    def write_readme(self):
        with self.readme.open(mode="w") as f:
            f.write(self.generate())

    def generate(self) -> str:
        return self.formatting.separation_format.join(
                self.formatting.language_format.format(
                    **tomllib.loads(lang.read_text())
                    )
                for lang in self.langs_dir.iterdir()
                if lang.suffix == ".toml"
                )
