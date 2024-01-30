# flask-cache-test

Test the functionality of the `Cache-Control: max-age` header

![A screenshot of loading](screenshot.png)

## Requirements

- [pyenv](https://github.com/pyenv/pyenv)

## Setup

```bash
$ ./scripts/setup
```

## Development

NOTE: You must use `127.0.0.1` rather than `localhost`.

### Ports

| Service           | Port                            |
| ----------------- | ------------------------------- |
| Flask app         | [`5002`](http://127.0.0.1:5002) |

## Scripts

| Name     | Description                        |
|----------|------------------------------------|
| `format` | Run black on all Python files      |
| `server` | Run the application                |
| `setup`  | Set up the development environment |
| `update` | Install dependencies               |
