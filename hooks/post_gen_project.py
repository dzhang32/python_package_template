import os
import shutil

# Remove docs files if not needed
if '{{cookiecutter.include_docs}}' != 'y':
    if os.path.exists('docs'):
        shutil.rmtree('docs')
    if os.path.exists('mkdocs.yml'):
        os.remove('mkdocs.yml')

# Remove CLI file if not needed
if '{{cookiecutter.include_cli}}' != 'y':
    cli_file = 'src/{{cookiecutter.package_name}}/__main__.py'
    if os.path.exists(cli_file):
        os.remove(cli_file)
