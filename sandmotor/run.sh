#!/bin/bash

source ~/.envs/aeolis/bin/activate

for var in "$@"
do
    aeolis "$var"
done
