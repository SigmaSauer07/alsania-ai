#!/bin/bash
DATASET_FILE="../dataset/dataset.json"

# Add dataset to IPFS
CID=$(ipfs add -q $DATASET_FILE)

# Publish to IPNS
ipfs name publish $CID
