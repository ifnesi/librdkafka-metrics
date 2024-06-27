#!/bin/bash

function logging() {
  TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S.000"`
  LEVEL=${2-"INFO"}
  if [[ $3 == "-n" ]]; then
    echo -n "[stop_demo] $TIMESTAMP [$LEVEL]: $1"
  else
    echo "[stop_demo] $TIMESTAMP [$LEVEL]: $1"
  fi
}

echo ""
logging "Stopping docker compose"
if docker compose down ; then
    kill -9 $(ps aux | grep 'pycrm:app' | awk '{print $2}') >/dev/null 2>&1
    logging "Demo successfully stopped"
    echo ""
    exit 0
else
    logging "Please start Docker Desktop!" "ERROR"
    echo ""
    exit -1
fi