#!/bin/bash

podman run --rm --name=unit-tests --mount type=bind,source=$PWD,target=/project unit-tests unit-test-executor/scripts/entry-point.sh "$@"
