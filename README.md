# HUD.ai Python Client
[![Build Status][ci-badge]][ci-url]
[![PyPI][pypi-badge]][pypi-url]
[![License][license-badge]]()

The HUD.ai Python Client provides an easy to use wrapper to interact with the
HUD.ai API in python applications.

You must first acquire a HUD.ai secret key before you can use this module.

## Installation

`pip install hudai`

## Usage

```python
from hudai.client import HudAi

client = HudAi('your-api-token-here')

# Alternatively, if you're working with a non-production environment
# client = HudAi('your-api-token-here', base_url='https://stage.api.hud.ai')

client.company.list()

client.news_api_article.get('17787d76-4198-4775-a49a-b3581c37a482')
```

## Deployment

Deploys occur automatically via Travis-CI on tagged commits that build
successfully. Should you need to manually build the project, follow these steps:

```bash
# Install twine to prevent your password from being set in plaintext
pip install twine
# Build the package
python setup.py sdist
# Upload via twine
twine upload dist/hudai-NEW_VERSION_HERE.tar.gz
```


[ci-badge]: https://travis-ci.org/FoundryAI/hud-ai-python.svg?branch=master
[ci-url]: https://travis-ci.org/FoundryAI/hud-ai-python
[pypi-badge]: https://img.shields.io/pypi/v/hudai.svg
[pypi-url]: https://pypi.python.org/pypi/hudai
[license-badge]: https://img.shields.io/pypi/l/hudai.svg
