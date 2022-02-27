#!/usr/bin/env bash

cd env_sim
maturin develop
cd ..
python3 all_animal.py &
python3 rendering.py
