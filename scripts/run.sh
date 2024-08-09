#!/bin/sh

# Run all development servers and services

trap killchildren SIGINT

killchildren() {
    echo "Shutting down dev servers..."
    kill -15 0
}

# Run litestar server (port 8000)
litestar --app server.app:app run --reload

# # Run vite server (port 3000)
# npm run dev &

# wait
