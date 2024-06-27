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
import logging
import argparse

from configparser import ConfigParser
from confluent_kafka import Consumer, KafkaException
from prometheus_client import start_http_server
from confluent_kafka.serialization import StringDeserializer

from utils import ConsumerMetricsManager


def main(args):
    kconfig = ConfigParser()
    kconfig.read(os.path.join(args.config))

    # Configure Kafka consumer
    librdkafka_callback = ConsumerMetricsManager()
    consumer_config = {
        "group.id": args.group_id,
        "client.id": args.client_id,
        "auto.offset.reset": args.offset_reset,
        # Set librdkafka metric
        "statistics.interval.ms": 5000,
        "stats_cb": librdkafka_callback.send,
    }
    consumer_config.update(dict(kconfig["kafka"]))
    consumer = Consumer(consumer_config)

    string_deserializer = StringDeserializer("utf_8")

    try:
        consumer.subscribe([args.topic])
        logging.info(
            f"Started consumer {consumer_config['client.id']} ({consumer_config['group.id']}) on topic '{args.topic}'"
        )

        while True:
            try:
                msg = consumer.poll(timeout=0.25)
                if msg is not None:
                    if msg.error():
                        raise KafkaException(msg.error())
                    else:
                        logging.info(
                            f"Key: {string_deserializer(msg.key())} | Value = {string_deserializer(msg.value())}"
                        )
            except Exception as err:
                logging.error(err)

            except KeyboardInterrupt:
                logging.info("CTRL-C pressed by user!")
                break

    except Exception as err:
        logging.error(err)
    finally:
        logging.info(
            f"Closing consumer {consumer_config['client.id']} ({consumer_config['group.id']})"
        )
        consumer.close()


if __name__ == "__main__":
    logging.basicConfig(
        format="%(asctime)s.%(msecs)03d [%(levelname)s]: %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    parser = argparse.ArgumentParser(description="Python Consumer")
    DEFAULT_CONFIG = os.path.join("config", "localhost.ini")
    OFFSET_RESET = [
        "earliest",
        "latest",
    ]
    parser.add_argument(
        "--topic",
        help="Topic name",
        dest="topic",
        type=str,
        default="demo_data",
    )
    parser.add_argument(
        "--config",
        dest="config",
        type=str,
        help=f"Select config filename for additional configuration, such as credentials (default: {DEFAULT_CONFIG})",
        default=DEFAULT_CONFIG,
    )
    parser.add_argument(
        "--offset-reset",
        dest="offset_reset",
        help=f"Set auto.offset.reset (default: {OFFSET_RESET[0]})",
        type=str,
        default=OFFSET_RESET[0],
        choices=OFFSET_RESET,
    )
    parser.add_argument(
        "--group-id",
        dest="group_id",
        type=str,
        help=f"Consumer's Group ID (default is 'consumer-client')",
        default="consumer-client",
    )
    parser.add_argument(
        "--client-id",
        dest="client_id",
        type=str,
        help=f"Consumer's Client ID (default is 'consumer-client-01')",
        default="consumer-client-01",
    )
    parser.add_argument(
        "--port",
        dest="port",
        type=int,
        help="HTTP Server Port (Default 8002)",
        default=8002,
    )
    args = parser.parse_args()

    logging.info(f"Starting HTTP Server on port: {args.port}")
    start_http_server(args.port)

    main(args)
