# Contributing to programming-language-navigator
---

## Prerequisites

1. [Fork the repository](https://github.com/wyasher/programming-language-navigator/fork)
2. Clone your forked repo:
```sh
git clone https://github.com/$GITHUB_USERNAME/programming-language-navigator
```
3. Cd in your project:
```sh
cd programming-language-navigator
```
---

## Contribution ways

### Adding a new programming language to the list

**Adding languages using the script:**

```sh
# Pass the data as arguments
python run.py -l LangName \
    "Language long description..." \
    https://lang-website.org \
    https://github.com/lang/lang-repo

# Add language interactively
python run.py -i
*) Input name: LangName
*) Input description: Language long description...
*) Input website: https://lang-website.org
*) Input repository: https://github.com/lang/lang-repo
```

**Add languages by hand**

1. Copy the template into new file
```sh
cp langs/TEMPLATE.toml langs/LangName.toml
```
2. Edit the .toml file

### Generating README
**! Always use the script, do not update readme by hand**
```sh
python run.py -r
```
