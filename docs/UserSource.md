# UserSource

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`                  | String     | Resource ID **Cannot be edited** |
| `user_id`* 	        | **String** | Associated user |
| `source_id`*          | **String** | Associated source |
| `reliability_score`*  | **Float**  | Reliability score for source between 0 and 1 |


## `client.user_sources.list(user_id?, source_id?, page?)`

## `client.user_sources.create(user_id, source_id, reliability_score)`

## `client.user_sources.update(user_id, source_id, reliability_score?)`

## `client.user_sources.delete(user_id, source_id)`
