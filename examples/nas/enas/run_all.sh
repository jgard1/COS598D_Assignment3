#!/bin/bash
python3 retrain.py --arc-checkpoint ./checkpijts/epoch_49.json --search-for micro
python3 search.py --search-for micro --v1 --visualization