#!/bin/bash

# Pull the latest Grobid lightweight image
docker pull lfoppiano/grobid:0.8.0

# Start the Grobid lightweight container
docker run -d --name grobid_lightweight --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0

echo "Grobid lightweight container started. Access it at http://localhost:8070"
