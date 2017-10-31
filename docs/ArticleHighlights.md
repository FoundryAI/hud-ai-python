# ArticleHighlights

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          | String     | Resource ID **Cannot be edited** |
| `article_id`* | **String** | Article being highlighted |
| `body`*       | **String** | Phrases that should be highlighted |
| `user_id`*    | **String** | User the highlights apply to |

## `client.article_highlights.list(article_id?, link_hash?, user_id?, page?)`

**NOTE:** `link_hash` is MD5 hash of the article URL

## `client.article_highlights.create(**params)`

Takes all of the model attributes as keyword params

## `client.article_highlights.fetch(id)`

## `client.article_highlights.update(id, **params)`

Takes all of the model attributes as keyword params

## `client.article_highlights.delete(id)`
