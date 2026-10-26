# Data schema

`data/apps.csv` and `data/apps.json` carry the same fields.

| Field | Type | Required | Notes |
|---|---|---|---|
| `name` | string | yes | App name as shown on the store |
| `package` | string | no | Android package id. Unique when present. |
| `developer` | string | no | Developer or company |
| `category` | string | yes | Must be one of the categories in CONTRIBUTING.md |
| `play_category` | string | no | Standard Google Play category, or empty |
| `play_url` | string | no | Exact listing link, or a search link if the package is unknown |
| `website_url` | string | no | Official site, mainly for apps that are not on Play |
| `open_source` | enum | yes | `Yes` / `No` / `Unknown` |
| `status` | enum | yes | `Active` / `Unknown` |
| `has_icon` | enum | yes | `Yes` / `No` |

## Example row

```json
{
  "name": "Zoho Mail",
  "package": "com.zoho.mail",
  "developer": "Zoho Corporation",
  "category": "Zoho Apps",
  "play_category": "Productivity",
  "play_url": "https://play.google.com/store/apps/details?id=com.zoho.mail",
  "website_url": "",
  "open_source": "Unknown",
  "status": "Active",
  "has_icon": "Yes"
}
```
