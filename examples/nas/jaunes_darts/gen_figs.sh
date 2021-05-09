#!/usr/bin/env bash
python extract_and_graph.py main_epoch_0.txt "Stage 1 Complete" ./figs/
python extract_and_graph.py main_epoch_1.txt "Stage 2 Complete" ./figs/
python extract_and_graph.py main_epoch_2.txt "Stage 3 Complete" ./figs/
python extract_and_graph.py 0_epoch_25.txt "Stage 1 Epoch 25" ./figs/
python extract_and_graph.py 0_epoch_50.txt "Stage 1 Epoch 50" ./figs/
python extract_and_graph.py 1_epoch_25.txt "Stage 2 Epoch 25" ./figs/
python extract_and_graph.py 1_epoch_50.txt "Stage 2 Epoch 50" ./figs/
python extract_and_graph.py 2_epoch_25.txt "Stage 3 Epoch 25" ./figs/
python extract_and_graph.py 2_epoch_50.txt "Stage 3 Epoch 50" ./figs/