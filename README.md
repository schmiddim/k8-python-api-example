[![Python application](https://github.com/schmiddim/k8-python-api-example/actions/workflows/python-app.yaml/badge.svg)](https://github.com/schmiddim/k8-python-api-example/actions/workflows/python-app.yaml)

## Write and Consume Kubernetes Configmaps

## Setup

deploy to a microk8s cluster (registry enabled)
# Run 

## Run on localhost

```
FLASK_ENV=development; flask run -h 0.0.0 -p 8080
```

## Tests

```
PYTHONPATH=. pytest tests/
```

## K8
```
kubectl apply -k kubernetes
```
## build container

```
VERSION=1.0;docker build . -t localhost:32000/python3k8api:v$VERSION;docker push localhost:32000/python3k8api:v$VERSION
```

# Testing
- @see https://github.com/pluralsight/intro-to-pytes
- @see https://testdriven.io/blog/testing-python/
