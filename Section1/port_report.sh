#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <IP>"
    exit 1
fi

IP=$1
DATE=$(date +%F)
OUTPUT="scan_${IP}_${DATE}.txt"

PORTS=(21 22 80 443 3306)
OPEN_COUNT=0

echo "Scanning $IP..." > $OUTPUT

for PORT in "${PORTS[@]}"; do
    timeout 1 bash -c "echo > /dev/tcp/$IP/$PORT" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Port $PORT: OPEN" | tee -a $OUTPUT
        ((OPEN_COUNT++))
    else
        echo "Port $PORT: CLOSED" >> $OUTPUT
    fi
done

echo "Total Open Ports: $OPEN_COUNT" | tee -a $OUTPUT
