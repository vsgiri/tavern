#!/bin/sh

set -ex

TAG=$(git describe --abbrev=0);

for dockertype in alpine slim-jessie; do
    for tagname in $TAG latest; do
        docker build --build-arg TAVERNVER=$TAG --file docker/Dockerfile.$dockertype --tag tavern:$tagname .
        # docker push tavern:$tagname
    done
done
