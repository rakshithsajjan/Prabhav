#!/bin/bash

# Navigate to your application directory (if necessary)
cd prabhav/

# virtual env
python3 -m venv venv && source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# Start Gunicorn
# Adjust the number of workers and threads as necessary
gunicorn --workers 4 --bind 0.0.0.0:8000 --env server:app