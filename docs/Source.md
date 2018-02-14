# Source

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`                    | String     | Resource ID **Cannot be edited** |
| `domain`*               | **String** | Source domain |
| `name`*                 | **String** | Source name |
| `reliability_score`     | Float      | Reliability score for source between 0 and 1 |
| `description`           | String     | Source description |
| `language`              | String     | Language of source |
| `country`               | String     | Country source is based in |

## `client.sources.list(domain?, name?, min_reliability?, max_reliability?, article_id?, page?)`

## `client.sources.create(**params)`

Takes all of the model attributes as keyword params

## `client.sources.fetch(id)`

## `client.sources.update(id, **params)`

Takes all of the model attributes as keyword params

## `client.sources.delete(id)`
