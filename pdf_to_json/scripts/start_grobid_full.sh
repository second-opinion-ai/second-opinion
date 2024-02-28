#!/bin/bash

# Pull the latest Grobid full image
docker pull grobid/grobid:0.8.0

# Start the Grobid full container
docker run -d --name grobid_full --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0

echo "Grobid full container started. Access it at http://localhost:8070"
