# campus-net

FAKE THURSDAY UNIVERSITY NETWORK

See <http://net.cqqqwq.com>

## Project setup

```
npm install
pip install -r requirements.txt
```

## Develop

### Lints and fixes files

```
npm run lint
```

## Deploy

Two ways:

1. Local deploy with Node & python
2. Deploy with docker

### Local Deploy

1. Compiles Static files(frontend)

```
npm run build
```

2. Setup Flask server(backend)

```
python3 main.py
```

### Docker Deploy

build image:

```bash
docker build campus-net .
```

run container

```bash
docker run -dp 5000:5000 campus-net 
```