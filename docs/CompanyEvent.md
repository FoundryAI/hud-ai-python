# CompanyEvent

| Attribute | Type | Description |
| --------- | ---- | ----------- |
| `id`          | String     | Resource ID **Cannot be edited** |
| `title`*      | **String** | Name of the event for display/search purposes |
| `description` | String     | Term (can be word or phrase) to find in articles |
| `event_type`* | **String** | Used for filtering (e.g. `earnings_call`) |
| `link_url`    | String     | Optional link to the event/more robust description |
| `starts_at`*  | **Date**   | When does this event start |
| `ends_at`*    | **Date**   | When does this event end |

## `client.company_events.list(company_id, starting_before?, starting_after?, ending_before?, ending_after?, occurring_at?, title?, event_type?, page?)`

## `client.company_events.create(**params)`

Takes all of the model attributes as keyword params

## `client.company_events.fetch(company_id, event_id)`

## `client.company_events.update(company_id, event_id, **params)`

Takes all of the model attributes as keyword params

## `client.company_events.delete(company_id, event_id)`
