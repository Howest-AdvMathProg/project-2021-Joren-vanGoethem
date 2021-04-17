# Search

When sending this event to the server make sure your message object has the following format.

## Base Object

Exact defines if the search can contain the query or be an exact match.

```json
{
  "event": "SEARCH",
  "data": {
    "query": {},
    "type": "",
    "exact": false
  }
}
```

### Search All

This searches for any value in all of the columns.

```json
{
  "event": "SEARCH",
  "data": {
    "query": "",
    "type": "all",
    "exact": false
  }
}
```

### Search Column

Search for a value in a specific column.

```json
{
    "event": "SEARCH",
    "data": {
        "query": {
            "column": "",
            "value": ""
        },
        "type": "column",
        "exact": false
    }
}
```

### Search Columns

This searches for any value in all of the columns.

```json
{
    "event": "SEARCH",
    "data": {
        "query": {
            "columns": [""],
            "values": [""]
        },
        "type": "columns",
        "exact": false
    }
}
```