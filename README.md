## Write and Consume Kubernetes Configmaps

## Setup
deploy to a microk8s cluster (registry enabled)

## build container
```
VERSION=1.0;docker build . -t localhost:32000/python3k8api:v$VERSION;docker push localhost:32000/python3k8api:v$VERSION
```