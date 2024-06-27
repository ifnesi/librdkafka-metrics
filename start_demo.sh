#!/bin/bash

function logging() {
  TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S.000"`
  LEVEL=${2-"INFO"}
  if [[ $3 == "-n" ]]; then
    echo -n "[start_demo] $TIMESTAMP [$LEVEL]: $1"
  else
    echo "[start_demo] $TIMESTAMP [$LEVEL]: $1"
  fi
}

logging "Starting docker compose"
if ! docker compose up -d --build ; then
    logging "Please start Docker Desktop!" "ERROR"
    exit -1
fi

# Waiting services to be ready
logging "Waiting Schema Registry to be ready" "INFO" -n
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' http://localhost:8081)" != "200" ]]
do
    echo -n "."
    sleep 1
done

echo ""
logging "Waiting Confluent Control Center to be ready" "INFO" -n
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' http://localhost:9021)" != "200" ]]
do
    echo -n "."
    sleep 1
done

# Open browser with C3, Prometheus and Grafana
python3 -m webbrowser -t "http://localhost:9021/clusters"
python3 -m webbrowser -t "http://localhost:3000"
python3 -m webbrowser -t "http://localhost:9090/targets?search="

logging "Demo successfully started"

echo ""