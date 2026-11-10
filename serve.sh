#!/usr/bin/env bash
# Serve the harness locally. Open http://localhost:8000/ui/
cd "$(dirname "$0")" && exec python3 -m http.server 8000 --bind 127.0.0.1
