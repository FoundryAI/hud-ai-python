# HUD.ai Python Client
[![Build Status][ci-badge]][ci-url]
[![PyPI][pypi-badge]][pypi-url]
[![PyPI][python-versions-badge]][pypi-url]
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
| `id`               | String          | Resource ID **Cannot be edited** |
| `authors`          | Array\<String\> | List of author names |
| `image_url`        | String          | Image published in the article's metadata |
| `importance_score` | Number          | `hudai-importance-scorer` output |
| `link_hash`        | String          | MD5 hash of the `link_url` **Cannot be edited** |
| **`link_url`**     | **String**      | Where the article was originally published |
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
- `link_hash`
- `published_after`
- `published_before`
- `type`

Example:
```
client.article.list(type='rss', published_after='2017-07-26T18:18:58Z')
```

#### `client.article.create(**params)`

Takes all of the model attributes as keyword params (except `link_hash`)

#### `client.article.get(id)`

#### `client.article.update(id, **params)`

Takes all of the model attributes as keyword params (except `link_hash`)

#### `client.article.delete(id)`

#### `client.article.key_terms(id)`

Returns a list of key terms (`String`) associated with the article


### ArticleHighlights

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`article_id`** | **String** | Article being highlighted |
| **`body`**       | **String** | Phrases that should be highlighted |
| **`user_id`**    | **String** | User the highlights apply to |

#### `client.article_highlights.list(**params)`

Optional Params:
- `article_id`
- `link_hash` MD5 hash of the article URL
- `user_id`

#### `client.article_highlights.create(**params)`

Takes all of the model attributes as keyword params

#### `client.article_highlights.get(id)`

#### `client.article_highlights.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.article_highlights.delete(id)`


### ArticleKeyTerm

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`article_id`** | **String** | Article identifier |
| **`key_term`**   | **String** | Key term in article |

#### `client.article_key_term.list(**params)`

Optional Params:
- `key_term`
- `article_id`

#### `client.article_key_term.create(**params)`

Takes all of the model attributes as keyword params

#### `client.article_key_term.get(id)`

#### `client.article_key_term.delete(id)`


### Company

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`       | String     | Resource ID **Cannot be edited** |
| **`name`** | **String** | Primary company name (others can be associated as key terms) |

#### `client.company.list()`

#### `client.company.create(**params)`

Takes all of the model attributes as keyword params

#### `client.company.get(id)`

#### `client.company.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.company.delete(id)`

#### `client.company.domains(id)`

Lists all `Domain`s (hostnames) associated with the company

#### `client.company.key_terms(id)`

Lists all `KeyTerm`s associated with the company


### CompanyKeyTerm

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`company_id`** | **String** | Associated company |
| **`term`**       | **String** | Term (can be word or phrase) to find in articles |

#### `client.company_key_term.list(**params)`

Optional Params:
- `company_id`

#### `client.company_key_term.create(**params)`

Takes all of the model attributes as keyword params

#### `client.company_key_term.get(id)`

#### `client.company_key_term.delete(id)`


### Domain

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`company_id`** | **String** | Associated company |
| **`hostname`**   | **String** | FQDN e.g. `api.hud.ai` |

#### `client.domain.list(**params)`

Optional Params:
- `company_id`
- `hostname`

#### `client.domain.create(**params)`

Takes all of the model attributes as keyword params

#### `client.domain.get(id)`

#### `client.domain.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.domain.delete(id)`


### KeyTerm

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| **`term`** | **String** | Term (can be word or phrase) to find in articles |

#### `client.key_term.list(**params)`

Optional Params:
- `page`

#### `client.key_term.create(**params)`

Takes all of the model attributes as keyword params

#### `client.key_term.get(term)`

#### `client.key_term.delete(term)`


### System Event

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          | String     | Resource ID **Cannot be edited** |
| **`name`**    | **String** | Event identifier e.g. `article.processed` |
| **`payload`** | **Dictionary** | Event payload e.g. `{'location': 's3://my-bucket/file-path', type:'rss'}` |

#### `client.system_event.list(**params)`

Optional Params:
- `page`

#### `client.system_event.create(**params)`

Takes all of the model attributes as keyword params

#### `client.system_event.get(id)`


### System Task

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`           | String     | Resource ID **Cannot be edited** |
| **`task_id`**  | **String** | Task identifier (typically from `celery`) |
| `attempts`     | Number     | How many times has this job been started |
| `started_at`   | Date       | Last time that the job was attempted |
| `completed_at` | Date       | When the job finished (irregardless of success) |

#### `client.system_task.list(**params)`

Optional Params:
- `task_id`
- `page`
- `started_after`
- `started_before`
- `completed` (Boolean)

#### `client.system_task.create(**params)`

Takes all of the model attributes as keyword params

#### `client.system_task.get(id)`

#### `client.system_task.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.system_task.delete(id)`


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
[python-versions-badge]: https://img.shields.io/pypi/pyversions/hudai.svg
[license-badge]: https://img.shields.io/pypi/l/hudai.svg
