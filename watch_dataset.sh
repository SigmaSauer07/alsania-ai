#!/bin/bash

# Path to your dataset file
DATASET_FILE="dataset/dataset.json"

echo "Watching for changes in $DATASET_FILE..."

# Ensure inotify-tools is installed
sudo apt-get install inotify-tools -y

# Watch for file modifications
inotifywait -m -e close_write $DATASET_FILE |
while read path action file; do
    echo "Dataset updated, converting to IPLD and publishing to IPFS..."

    # Convert the dataset to IPLD (DAG format)
    IPLD_CID=$(ipfs dag put $DATASET_FILE)

    # Publish the IPLD CID to IPNS
    ipfs name publish --allow-offline $IPLD_CID

    echo "Published new dataset with IPLD CID: $IPLD_CID"

    # Update ChromaDB with new vector embeddings
    echo "Updating vector database..."
    python3 process_dataset.py
done
