# {{cookiecutter.package_name}}

{{cookiecutter.description}}

## Installation

I recommend using [uv](https://docs.astral.sh/uv/) to manage the python version, virtual environment and `{{cookiecutter.package_name}}` installation:

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install {{cookiecutter.package_name}}
# Install Chromium browser binary required for playwright.
playwright install chromium
```