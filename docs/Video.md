# Video

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`               | String         | Resource ID **Cannot be edited** |
| `created_at`       | Date           | Date created |
| `updated_at`       | Date           | Date updated |
| `title`*           | **String**     | Title of the video |
| `description`      | String         | Description of the video |
| `transcript`       | String         | Transcript of the video |
| `importance_score`*| **Number**     | `hudai-importance-scorer` output |
| `poster_url`       | String         | Poster preview image   |
| `video_url`*       | **String**     | Video url link for playing  |
| `published_at`*    | **Date**       | Original publishing date |
| `source_id`        | String         | Source identifier |

## `client.videos.search(text?, person_id?, max_importance?, min_importance?, company_id?, source_id?, page?, published_after?, published_before?, created_after?, created_before?)`

## `client.videos.list(person_id?, importance_score_min?, company_id?, source_id?, page?, published_after?, published_before?)`

Example:

```python
last_week = datetime.datetime.now() - datetime.timedelta(days=7)

client.videos.list(published_after=last_week)
```

## `client.videos.create(**params)`

## `client.videos.fetch(id)`

## `client.videos.update(id, **params)`

## `client.videos.delete(id)`
