# Identify

Once you're connected to the server your client needs to send an IDENTIFY event with the user making the connection.

## Base Object

```json
{
    "event": "IDENTIFY",
    "data": {
        "nick": "Yimura",
        "name": "Andreas Maerten",
        "mail": "andreas.maerten@scarlet.be"
    }
}
```