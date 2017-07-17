# HUD.ai Python Client

The HUD.ai Python Client provides an easy to use wrapper to interact with the HUD.ai API in python applications.

You must first acquire a HUD.ai secret key before you can use this module.

## Installation

`pip install hudai`

## Usage

```python
from hudai.client import HudAi

client = HudAi('your-api-token-here')

client.company.list()

client.news_api_article.get('17787d76-4198-4775-a49a-b3581c37a482')
```

## Deployment
First you must build the app
```bash
python setup.py sdist
```

Then upload it via twine
```bash
twine upload dist/hudai-NEW_VERSION_HERE.tar.gz
```
