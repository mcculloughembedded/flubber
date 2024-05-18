#!/bin/bash

podman run --rm --name=unit-tests --mount type=bind,source=$PWD,target=/project unit-tests flubber/scripts/entry-point.sh "$@"
