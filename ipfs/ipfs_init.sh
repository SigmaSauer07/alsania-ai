#!/bin/bash
export IPFS_PATH="$HOME/.ipfs"
ipfs daemon --enable-pubsub-experiment &
