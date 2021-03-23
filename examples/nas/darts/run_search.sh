#!/bin/bash
python3 search.py --v1 --visualization
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_49.json
