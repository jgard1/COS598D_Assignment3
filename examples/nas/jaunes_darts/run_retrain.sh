#!/usr/bin/env bash
python search.py > pdarts_search_output.txt
# python retrain.py --arc-checkpoint "./checkpoints/epoch_0.json" > "./main_epoch_0.txt"
# python retrain.py --arc-checkpoint "./checkpoints/epoch_1.json" > "./main_epoch_1.txt"
python retrain.py --arc-checkpoint "./checkpoints/epoch_2.json" > "./main_epoch_2.txt"
# python retrain.py --arc-checkpoint "./checkpoints_0/epoch_50.json" > "./0_epoch_50.txt"
# python retrain.py --arc-checkpoint "./checkpoints_1/epoch_50.json" > "./1_epoch_50.txt"
# python retrain.py --arc-checkpoint "./checkpoints_2/epoch_50.json" > "./2_epoch_50.txt"
# python retrain.py --arc-checkpoint "./checkpoints_0/epoch_25.json" > "./0_epoch_25.txt"
# python retrain.py --arc-checkpoint "./checkpoints_1/epoch_25.json" > "./1_epoch_25.txt"
# python retrain.py --arc-checkpoint "./checkpoints_2/epoch_25.json" > "./2_epoch_25.txt"