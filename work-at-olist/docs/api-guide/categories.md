# Categories

## List by Channel

List all categories by channel name endpoint.

`GET /channels/<channel-name>/categories/`

Success response:

```html
HTTP 200 OK
```

```json
[
    {
        "name": "Test",
        "parent": null,
        "subcategories": [
            {
                "name": "Teste"
            }
        ]
    },
    {
        "name": "Teste",
        "parent": {
            "name": "Test"
        },
        "subcategories": []
    }
]
```

## Retrieve

Retrieve a category endpoint.

`GET /channels/categories/<category-name>/`

Success response:

```html
HTTP 200 OK
```

```json
{
    "name": "Test",
    "parent": null,
    "subcategories": [
        {
            "name": "Teste"
        }
    ]
}
```
