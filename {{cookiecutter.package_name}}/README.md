# {{cookiecutter.package_name}}

{{cookiecutter.description}}

## Installation

I recommend using [uv](https://docs.astral.sh/uv/) to manage the python version, virtual environment and `{{cookiecutter.package_name}}` installation:

```bash
uv venv --python 3.13
source .venv/bin/activate
uv pip install {{cookiecutter.package_name}}
```

## Additional setup

### Code coverage

- Add a "CODECOV_TOKEN" secret (obtained from [here](https://app.codecov.io/gh/dzhang32/test_python_package/)) to your repo via `Settings` -> `Secrets and variables` -> `Actions`. 

{% if cookiecutter.include_docs == 'y' %}
### Deploying docs to gh-pages

1. Go to your repository's `Settings` -> `Actions` -> `General`.
2. Scroll to `Workflow permissions` and allow GHA to have `Read and write permissions` so it can create/push to the `gh-pages` branch.
3. Go to `Settings` -> `Pages`.
4. Configure your repo to deploy from the root of `gh-pages` branch.

{% endif %}

{% if cookiecutter.include_pypi == 'y' %}
### Deploying to PyPI

- Go to your [PyPi publishing settings](https://pypi.org/manage/account/publishing/) and fill in the following details:

    - **PyPI Project Name:** {{cookiecutter.package_name}}
    - **Owner:** {{cookiecutter.github_username}}
    - **Repository name:** {{cookiecutter.package_name}}
    - **Workflow name:** test_deploy.yml
    - **Environment name:** (leave blank)

{% endif %}