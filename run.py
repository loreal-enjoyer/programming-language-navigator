import argparse
import commands


def main(args) -> None:
    if args.readme:
        commands.generate_readme()
    elif args.interactive:
        commands.generate_language()
    else:
        commands.generate_language(args.language)


def _italic(text: str) -> str:
    return f"\033[3m{text}\033[0m"


if __name__ == "__main__":
    language_params = " ".join(
            [_italic(param)
             for param in
             ["name", "description", "website", "repository"]]
            )

    parser = argparse.ArgumentParser(
            prog="generator",
            usage="%(prog)s" +
            f" [-i / -r / -l {language_params}]")

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-i", "--interactive", action="store_true",
                       help="Add a new language interactively")
    group.add_argument("-r", "--readme", action="store_true",
                       help="Generate README from sources", dest="readme")
    group.add_argument("-l", "--lang", "--language", nargs=4,
                       help=f"Add a new language with specified {language_params}",
                       dest="language")

    exit(main(parser.parse_args()))
