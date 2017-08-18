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

client.article.fetch('17787d76-4198-4775-a49a-b3581c37a482')
```

***DOCUMENTATION NOTES***

- `Date` types are automatically converted to/from standard `DateTime` objects
- Bolded `Type`s indicate that the field is required
- All `list` resources are paginated to 50/request, with `page` being 0-indexed (e.g. `page=3` will get you the fourth page)
- Params indicated with `?` are optional keyword params


### Article

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`               | String          | Resource ID **Cannot be edited** |
| `authors`          | list\<String\> | List of author names |
| `image_url`        | String          | Image published in the article's metadata |
| `importance_score` | Number          | `hudai-importance-scorer` output |
| `link_hash`        | String          | MD5 hash of the `link_url` **Cannot be edited** |
| **`link_url`**     | **String**      | Where the article was originally published (e.g. `https://www.nytimes.com/2017/08/01/world/middleeast/mosul-isis-survivors-rights.html`) |
| `published_at`     | Date            | Original publishing date |
| **`raw_data_url`** | **String**      | Location of raw feed content (e.g. JSON/HTML), this is typically an S3 location (e.g. `s3://raw-storage/2017/08/01/raw-article.json`) |
| **`source_url`**   | **String**      | URL of the publication source (e.g. `https://newsapi.org/v1/articles?source=the-wall-street-journal`) |
| `text`             | String          | Plaintext format of the article body |
| **`title`**        | **String**      | Title article was published as |
| **`article_type`** | **String**      | `rss` \| `newsApi` \| `facebook` \| `twitter` |

#### `client.article.list(article_type?, importance_score_min?, key_term?, link_hash?, page?, published_after?, published_before?)`

Example:

```python
last_week = datetime.datetime.now() - datetime.timedelta(days=7)

client.article.list(article_type='rss', published_after=last_week)
```

#### `client.article.create(**params)`

Takes all of the model attributes as keyword params (except `link_hash`)

#### `client.article.fetch(id)`

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

#### `client.article_highlights.list(article_id?, link_hash?, user_id?, page?)`

**NOTE:** `link_hash` is MD5 hash of the article URL

#### `client.article_highlights.create(**params)`

Takes all of the model attributes as keyword params

#### `client.article_highlights.fetch(id)`

#### `client.article_highlights.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.article_highlights.delete(id)`


### ArticleKeyTerm

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`article_id`** | **String** | Article identifier |
| **`term`**       | **String** | Key term in article |

#### `client.article_key_term.list(article_id, page?)`

#### `client.article_key_term.create(article_id, term)`

#### `client.article_key_term.fetch(article_id, term)`

#### `client.article_key_term.delete(article_id, term)`


### Company

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`       | String     | Resource ID **Cannot be edited** |
| **`name`** | **String** | Primary company name (others can be associated as key terms) |

#### `client.company.list(page?)`

#### `client.company.create(**params)`

Takes all of the model attributes as keyword params

#### `client.company.fetch(id)`

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

#### `client.company_key_term.list(company_id?, page?)`

#### `client.company_key_term.create(**params)`

Takes all of the model attributes as keyword params

#### `client.company_key_term.fetch(id)`

#### `client.company_key_term.delete(id)`


### Domain

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`company_id`** | **String** | Associated company |
| **`hostname`**   | **String** | FQDN e.g. `api.hud.ai` |

#### `client.domain.list(company_id?, hostname?, page?)`

#### `client.domain.create(**params)`

Takes all of the model attributes as keyword params

#### `client.domain.fetch(id)`

#### `client.domain.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.domain.delete(id)`


### KeyTerm

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| **`term`** | **String** | Term (can be word or phrase) to find in articles |

#### `client.key_term.list(page?)`

#### `client.key_term.create(**params)`

Takes all of the model attributes as keyword params

#### `client.key_term.fetch(term)`

#### `client.key_term.delete(term)`


### SystemEvent

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          | String         | Resource ID **Cannot be edited** |
| **`name`**    | **String**     | Event identifier e.g. `article.processed` |
| **`payload`** | **Dictionary** | Event payload e.g. `{'location': 's3://my-bucket/file-path', type:'rss'}` |

#### `client.system_event.list(page?)`

#### `client.system_event.create(**params)`

Takes all of the model attributes as keyword params

#### `client.system_event.fetch(id)`


### SystemTask

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`           | String     | Resource ID **Cannot be edited** |
| **`task_id`**  | **String** | Task identifier (typically from `celery`) |
| `attempts`     | Number     | How many times has this job been started |
| `completed_at` | Date       | When the job finished (irregardless of success) |
| `started_at`   | Date       | Last time that the job was attempted |

#### `client.system_task.list(completed?, started_after?, started_before?, task_id?, page?)`

#### `client.system_task.create(**params)`

Takes all of the model attributes as keyword params

#### `client.system_task.fetch(id)`

#### `client.system_task.fetch_by_task_id(task_id)`

#### `client.system_task.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.system_task.mark_complete(task_id, completed_at?)`

#### `client.system_task.delete(id)`


### TextCorpus

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`           | String     | Resource ID **Cannot be edited** |
| **`body`**     | **String** | Text blob to use for relevance matching |
| **`type`**     | **String** | Text origin e.g. `email` or `custom` |
| **`user_id`**  | **String** | User the corpus is used to identify articles for |

#### `client.text_corpus.list(type?, user_id?, page?)`

#### `client.text_corpus.create(**params)`

Takes all of the model attributes as keyword params

#### `client.text_corpus.fetch(id)`

#### `client.text_corpus.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.text_corpus.delete(id)`


### User

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`        | String     | Resource ID **Cannot be edited** |
| **`email`** | **String** | Primary email address for updates/notifications |
| **`name`**  | **String** | User's full name (used in emails and other communications) |
| `time_zone` | String     | [tz database][tz-database-link] time zone used to determine when to send notifications (defaults to `America/New_York`) |

#### `client.user.list(email?, digest_subscription_day?, digest_subscription_hour?, name?, key_term?, page?)`

#### `client.user.create(**params)`

Takes all of the model attributes as keyword params

#### `client.user.fetch(id)`

#### `client.user.update(id, **params)`

Takes all of the model attributes as keyword params

#### `client.user.delete(id)`


### UserCompany

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`             | String     | Resource ID **Cannot be edited** |
| **`company_id`** | **String** | Associated company |
| **`user_id`**    | **String** | Associated user |

#### `client.user_company.list(company_id?, user_id?, page?)`

#### `client.user_company.create(**params)`

Takes all of the model attributes as keyword params

#### `client.user_company.fetch(id)`

#### `client.user_company.delete(id)`


### UserDigestSubscription

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`              | String     | Resource ID **Cannot be edited** |
| **`day_of_week`** | **String** | `sunday` \| `monday` \| `tuesday` \| `wednesday` \| `thursday` \| `friday` \| `saturday` |
| **`iso_hour`**    | **String** | 24-hour hour e.g. `08` = 8am, `17` = 5pm |
| **`user_id`**     | **String** | Associated user |

#### `client.user_digest_subscription.list(user_id, day_of_week?, iso_hour?, page?)`

#### `client.user_digest_subscription.create(user_id, **params)`

Takes all of the model attributes as keyword params

#### `client.user_digest_subscription.fetch(user_id, digest_id)`

#### `client.user_digest_subscription.delete(user_id, digest_id)`


### UserKeyTerm

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          | String     | Resource ID **Cannot be edited** |
| **`term`**    | **String** | Term (can be word or phrase) to find in articles |
| **`user_id`** | **String** | Associated user |

#### `client.user_key_term.list(user_id?, term?, page?)`

#### `client.user_key_term.create(**params)`

Takes all of the model attributes as keyword params

#### `client.user_key_term.fetch(id)`

#### `client.user_key_term.delete(id)`


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
[tz-database-link]: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
