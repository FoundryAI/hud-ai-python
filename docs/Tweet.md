# Tweet

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          | String     | Resource ID **Cannot be edited** |
| `person_id`*       | **String** | Related person ID |
| `twitter_tweet_id`* | **Number** | Related twitter tweet ID |
| `text`*       | **String** | Tweet content |

## `client.tweets.list(person_id?, page?)`

## `client.tweets.create(**params)`

Takes all of the model attributes as keyword params

## `client.tweets.fetch(id)`

## `client.tweets.fetch_by_twitter_id(twitter_tweet_id)`

## `client.tweets.delete(id)`
