import pathlib
from dataclasses import dataclass


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
