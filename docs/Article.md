# Article

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`               | String         | Resource ID **Cannot be edited** |
| `authors`          | list\<String\> | List of author names |
| `image_url`        | String         | Image published in the article's metadata |
| `importance_score` | Number         | `hudai-importance-scorer` output |
| `link_hash`        | String         | MD5 hash of the `link_url` **Cannot be edited** |
| `link_url`*        | **String**     | Where the article was originally published (e.g. `https://www.nytimes.com/2017/08/01/world/middleeast/mosul-isis-survivors-rights.html`) |
| `published_at`     | Date           | Original publishing date |
| `raw_data_url`*    | **String**     | Location of raw feed content (e.g. JSON/HTML), this is typically an S3 location (e.g. `s3://raw-storage/2017/08/01/raw-article.json`) |
| `source_url`*      | **String**     | URL of the publication source (e.g. `https://newsapi.org/v1/articles?source=the-wall-street-journal`) |
| `text`             | String         | Plaintext format of the article body |
| `title`*           | **String**     | Title article was published as |
| `article_type`*    | **String**     | `rss` \| `newsApi` \| `facebook` \| `twitter` |

## `client.articles.list(article_type?, importance_score_min?, key_term?, link_hash?, page?, published_after?, published_before?)`

Example:

```python
last_week = datetime.datetime.now() - datetime.timedelta(days=7)

client.articles.list(article_type='rss', published_after=last_week)
```

## `client.articles.create(**params)`

Takes all of the model attributes as keyword params (except `link_hash`)

## `client.articles.fetch(id)`

## `client.articles.update(id, **params)`

Takes all of the model attributes as keyword params (except `link_hash`)

## `client.articles.delete(id)`

## `client.articles.key_terms(id)`

Returns a list of key terms (`String`) associated with the article
