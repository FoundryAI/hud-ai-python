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

client = HudAi(api_key='your-api-token-here')

# Alternatively, if you're working with a non-production environment
# client = HudAi(api_key='your-api-token-here', base_url='https://stage.api.hud.ai')

client.company.list()

client.news_api_article.get('17787d76-4198-4775-a49a-b3581c37a482')
```

***DOCUMENTATION NOTES***

- All `Date` types listed below are ISO-8601 formatted strings. e.g.
`2017-07-26T18:18:58Z`

- Bolded `Type`s indicate that the field is required

### Article

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `authors`          | Array\<String\> | List of author names |
| `image_url`        | String          | Image published in the article's metadata |
| `importance_score` | Number          | `hudai-importance-scorer` output |
| **`link_url`**     | **String**      | Where the article was orginally published |
| `published_at`     | Date            | Original publishing date |
| **`raw_data_url`** | **String**      | Location of raw feed content (e.g. JSON/HTML) |
| **`source_url`**   | **String**      | URL of the publication source |
| `text`             | String          | Plaintext format of the article body |
| **`title`**        | **String**      | Title article was published as |
| **`type`**         | **String**      | `rss` \| `newsApi` \| `facebook` \| `twitter` |

#### `client.article.list(**params)`

Optional Params:
- `importance_score_min`
- `key_term`
- `published_after`
- `published_before`
- `type`

Example:
```
client.article.list(type='rss', published_after='2017-07-26T18:18:58Z')
```

#### `client.article.create(**params)`

Takes all of the model attributes as keyword params

#### `client.article.get(id)`

#### `client.article.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.article.delete(id)`

#### `client.article.key_terms(id)`

Returns a list of key terms (`String`) associated with the article

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
