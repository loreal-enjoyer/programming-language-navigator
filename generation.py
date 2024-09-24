import pathlib
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
    language_format: str
    separation_format: str


class ReadmeGenerator:
    def __init__(self, root: pathlib.Path, formatting: Format):
        self.root = root
        self.formatting = formatting

    def generate():
        pass
