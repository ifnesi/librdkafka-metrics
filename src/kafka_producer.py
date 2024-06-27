#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020 Confluent Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import time
import random
import string
import logging
import argparse

from uuid import uuid4
from configparser import ConfigParser
from confluent_kafka import Producer
from prometheus_client import start_http_server
from confluent_kafka.serialization import StringSerializer

from utils import ProducerMetricsManager


def main(args):
    kconfig = ConfigParser()
    kconfig.read(os.path.join(args.config_filename))

    # Configure Kafka consumer
    librdkafka_callback = ProducerMetricsManager()
    producer_config = {
        "client.id": args.client_id,
        # Set librdkafka metric
        "statistics.interval.ms": 5000,
        "stats_cb": librdkafka_callback.send,
    }
    producer_config.update(dict(kconfig["kafka"]))
    producer = Producer(producer_config)

    string_serializer = StringSerializer("utf_8")

    logging.info(
        f"Started producer {producer_config['client.id']} on topic '{args.topic}'"
    )

    while True:
        producer.poll(0.0)
        try:
            key = "".join(random.choices(string.digits, k=10))
            value = uuid4().hex
            producer.produce(
                topic=args.topic,
                key=string_serializer(key),
                value=string_serializer(value),
            )
        except KeyboardInterrupt:
            logging.info("CTRL-C pressed by user!")
            break
        except Exception as err:
            logging.error(err)
        finally:
            time.sleep(0.001)

    logging.info("Flushing producer")
    producer.flush()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d [%(levelname)s]: %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    DEFAULT_CONFIG = os.path.join("config", "localhost.ini")
    parser = argparse.ArgumentParser(description="Python Producer")
    parser.add_argument(
        "--topic",
        help="Topic name",
        dest="topic",
        type=str,
        default="demo_data",
    )
    parser.add_argument(
        "--config-filename",
        dest="config_filename",
        type=str,
        help=f"Select config filename for additional configuration, such as credentials (default: {DEFAULT_CONFIG})",
        default=DEFAULT_CONFIG,
    )
    parser.add_argument(
        "--client-id",
        dest="client_id",
        type=str,
        help=f"Consumer's Client ID (default is 'producer-client-01')",
        default="producer-client-01",
    )
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        help="HTTP Server Port (Default 8001)",
        default=8001,
    )
    args = parser.parse_args()

    logging.info(f"Starting HTTP Server on port: {args.port}")
    start_http_server(args.port)

    main(args)
