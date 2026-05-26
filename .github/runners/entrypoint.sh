#!/bin/bash
set -e

# Run whatever command the container is given; drop to a shell if none.
if [ $# -eq 0 ]; then
    exec /bin/bash
else
    exec "$@"
fi
