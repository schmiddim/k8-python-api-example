## Write and Consume Kubernetes Configmaps

## Setup

deploy to a microk8s cluster (registry enabled)

## Run on localhost

```
FLASK_ENV=development; flask run -h 0.0.0 -p 8080
```

## Tests

```
PYTHONPATH=. pytest tests/
```

## build container

```
VERSION=1.0;docker build . -t localhost:32000/python3k8api:v$VERSION;docker push localhost:32000/python3k8api:v$VERSION
```