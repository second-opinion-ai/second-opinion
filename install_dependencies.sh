#!/bin/bash

# Check Python version
if ! python -c 'import sys; assert sys.version_info >= (3,9)' > /dev/null; then
    echo "Python version should be >= 3.9"
    exit 1
fi

# Update Python resources at the global level
python -m pip install --upgrade setuptools wheel pip

# Setup and activate virtual environment
python -m venv .venv
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment."
    exit 1
fi

python -m pip install --upgrade setuptools wheel pip

# Check and install requirements
if [ -f "requires/requirements.txt" ]; then
    python -m pip install -r requires/requirements.txt
fi

if [ -f "requires/dev.txt" ]; then
    python -m pip install -r requires/dev.txt
fi
