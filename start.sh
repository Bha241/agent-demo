#!/bin/bash

# Start FastAPI backend in the background on port 8000
echo "Starting FastAPI backend..."
uvicorn api.app:app --host 127.0.0.1 --port 8000 &

# Wait a few seconds for the backend to spin up
sleep 3

# Start Streamlit frontend on port 8501 (or the PORT env var provided by Azure)
echo "Starting Streamlit frontend..."
streamlit run streamlit_app.py --server.port ${PORT:-8501} --server.address 0.0.0.0
