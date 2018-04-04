# Company

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`     | String     | Resource ID **Cannot be edited** |
| `name`*  | **String** | Primary company name (others can be associated as key terms) |
| `ticker` | String     | Stock ticker (e.g. `"NASDAQ:TWTR"`) |

## `client.companies.list(name?, ticker?, key_term?, page?)`

## `client.companies.create(**params)`

Takes all of the model attributes as keyword params

## `client.companies.fetch(id)`

## `client.companies.update(id, **params)`

Takes all of the model attributes as keyword params

## `client.companies.delete(id)`

## `client.companies.domains(id)`

Lists all `Domain`s (hostnames) associated with the company

## `client.companies.key_terms(id)`

Lists all `KeyTerm`s associated with the company

## `client.companies.search(query_string)`

Searches for Companies
