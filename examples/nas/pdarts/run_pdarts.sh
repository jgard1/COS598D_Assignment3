#!/usr/bin/env bash
python search.py --v1 --visualization > darts_search_output.txt

CHECKPOINT_PREFIX="./checkpoints/epoch_"
CHECKPOINT_SUFFIX=".json"

OUTPUT_PREFIX="pdarts_final_retrain_"
OUTPUT_SUFFIX=".txt"

for EPOCH in "0" "20" "40" "60" "80" "99" "10" "30" "50" "70" "90"    ### Outer for loop ###
do
    CHECKPOINT="${CHECKPOINT_PREFIX}${EPOCH}${CHECKPOINT_SUFFIX}"
    OUTFILE="${OUTPUT_PREFIX}${EPOCH}${OUTPUT_SUFFIX}"
    python retrain.py --arc-checkpoint $CHECKPOINT > $OUTFILE
done

