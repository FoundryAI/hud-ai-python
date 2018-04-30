# Company

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`     | String     | Resource ID **Cannot be edited** |
| `name`*  | **String** | Conference name |
| `description` | String     | Conference description |
| `timezone` | String     | Timezone the conference start and end times at in |
| `startsAt` | Date     | Time conference starts at |
| `endsAt` | Date     | Time conference ends at |
| `createdAt` | Date     |  |
| `updatedAt` | Date     | |

## `client.conferences.list(name?, personId?, before?, after?)`

## `client.conferences.create(**params)`

Takes all of the model attributes as keyword params

## `client.conferences.fetch(id)`

## `client.conferences.update(id, **params)`

Takes all of the model attributes as keyword params

## `client.conferences.delete(id)`

