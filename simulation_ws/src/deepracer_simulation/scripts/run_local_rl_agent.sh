#!/usr/bin/env bash

set -ex

AGENT_PY_PATH=$1
export NODE_TYPE=SIMULATION_WORKER
export PYTHONPATH=$AGENT_PY_PATH:$PYTHONPATH

python3 -m markov.single_machine_training_worker