import pathlib
import generation

ROOT = pathlib.Path(".")
LANGUAGES_LOCATION = ROOT / "langs"
README = ROOT / "README.md"
FORMAT = generation.Format(
        "{name}" \
                "{description}\n" \
                "---\n" \
                "* [Official Website: {website}]({website})" \
                "* [Repository: {repository}]({repository})",
                separation_format = "\n"
                )
