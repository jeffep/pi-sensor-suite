#!/bin/bash
# Launch all sensor scripts in background

cd "$(dirname "$0")/scripts"

python3 bmp280.py &
python3 bme280.py &
python3 ds18b20.py &
python3 mcp3008.py &
python3 mq135.py &
python3 hc_sr501.py &

echo "All sensor scripts started."
