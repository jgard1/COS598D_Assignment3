#!/bin/bash

#python3 search.py --v1 --visualization
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_0.json > darts_epoch_0_data.txt
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_14.json > darts_epoch_14_data.txt
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_28.json > darts_epoch_28_data.txt
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_35.json > darts_epoch_35_data.txt
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_7.json > darts_epoch_7_data.txt
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_21.json > darts_epoch_21_data.txt
python3 retrain.py --arc-checkpoint ./checkpoints/epoch_42.json > darts_epoch_42_data.txt
