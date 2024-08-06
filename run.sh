#!/bin/bash

# Navigate to your application directory (if necessary)
cd prabhav/

# install dependencies
pip install -r requirements.txt

# Start Gunicorn
# Adjust the number of workers and threads as necessary
gunicorn --workers 4 --bind 0.0.0.0:8000 server:app