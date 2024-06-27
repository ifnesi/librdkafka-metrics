![image](docs/logo.png)

# librdkafka-metrics
Kafka client metrics with librdkafka integrated with Prometheus and Grafana

This is a work in progress!

Based on https://github.com/shakti-garg/prometheus_kafka_metrics

Prometheus Status
![image](docs/prometheus-target-status.png)

Grafana Producer Dashboard
![image](docs/grafana-dashboard-producer.png)

Grafana Consumer Dashboard
![image](docs/grafana-dashboard-consumer.png)


Producer Metrics (http://localhost:8001/metrics)
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 379.0
python_gc_objects_collected_total{generation="1"} 7.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 44.0
python_gc_collections_total{generation="1"} 4.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="8",patchlevel="17",version="3.8.17"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 4.87591936e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.9392896e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.71951240696e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 96.09
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 12.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP kafka_consumer_reply_queue Number of ops(callbacks, events, etc) waiting in queue to serve with poll
# TYPE kafka_consumer_reply_queue gauge
# HELP kafka_consumer_consumed_records_rate Average number of messages consumed (excluding ignored msgs) per second
# TYPE kafka_consumer_consumed_records_rate gauge
# HELP kafka_consumer_consumed_bytes_rate Average message bytes (including framing) consumed per second
# TYPE kafka_consumer_consumed_bytes_rate gauge
# HELP kafka_consumer_records_lag Number of messages consumer is behind producer on this partition
# TYPE kafka_consumer_records_lag gauge
# HELP kafka_producer_reply_queue Number of ops(callbacks, events, etc) waiting in queue to serve with poll
# TYPE kafka_producer_reply_queue gauge
kafka_producer_reply_queue{client_id="generic-avro-producer-01",type="producer"} 0.0
# HELP kafka_producer_queue_msg_cnt Current number of messages in prometheus_kafka_producer queues
# TYPE kafka_producer_queue_msg_cnt gauge
kafka_producer_queue_msg_cnt{client_id="generic-avro-producer-01",type="producer"} 2.0
# HELP kafka_producer_queue_msg_size Current total size of messages in prometheus_kafka_producer queues
# TYPE kafka_producer_queue_msg_size gauge
kafka_producer_queue_msg_size{client_id="generic-avro-producer-01",type="producer"} 64.0
# HELP kafka_producer_inflight_msg_cnt Number of messages in-flight to broker awaiting response
# TYPE kafka_producer_inflight_msg_cnt gauge
kafka_producer_inflight_msg_cnt{client_id="generic-avro-producer-01",type="producer"} 0.0
# HELP kafka_producer_queue_latency_avg Average Producer queue latency in milliseconds
# TYPE kafka_producer_queue_latency_avg gauge
kafka_producer_queue_latency_avg{client_id="generic-avro-producer-01",type="producer"} 3.5695178971820836
# HELP kafka_producer_broker_latency_avg Broker latency / round-trip time in milliseconds
# TYPE kafka_producer_broker_latency_avg gauge
kafka_producer_broker_latency_avg{client_id="generic-avro-producer-01",type="producer"} 0.8914092953523238
# HELP kafka_producer_batch_size_bytes_avg Average Batch sizes in bytes
# TYPE kafka_producer_batch_size_bytes_avg gauge
kafka_producer_batch_size_bytes_avg{client_id="generic-avro-producer-01",type="producer"} 234.15292353823088
# HELP kafka_producer_batch_size_avg Average Batch message counts
# TYPE kafka_producer_batch_size_avg gauge
kafka_producer_batch_size_avg{client_id="generic-avro-producer-01",type="producer"} 3.5337331334332833
# HELP kafka_producer_request_rate Average number of requests sent per second
# TYPE kafka_producer_request_rate gauge
kafka_producer_request_rate{client_id="generic-avro-producer-01",type="producer"} 125331.41994980247
# HELP kafka_producer_request_bytes_rate Average number of requests bytes sent per second
# TYPE kafka_producer_request_bytes_rate gauge
kafka_producer_request_bytes_rate{client_id="generic-avro-producer-01",type="producer"} 40952.609784121814
# HELP kafka_producer_response_rate Average number of responses received per second
# TYPE kafka_producer_response_rate gauge
kafka_producer_response_rate{client_id="generic-avro-producer-01",type="producer"} 133.32970857763786
# HELP kafka_producer_response_bytes_rate Average number of response bytes received per second
# TYPE kafka_producer_response_bytes_rate gauge
kafka_producer_response_bytes_rate{client_id="generic-avro-producer-01",type="producer"} 0.0
```

Consumer Metrics (http://localhost:8002/metrics)
```
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 130.0
python_gc_objects_collected_total{generation="1"} 28.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 44.0
python_gc_collections_total{generation="1"} 4.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="8",patchlevel="17",version="3.8.17"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 5.62794496e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.8454912e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.71951238744e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 107.96000000000001
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 15.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1.048576e+06
# HELP kafka_consumer_reply_queue Number of ops(callbacks, events, etc) waiting in queue to serve with poll
# TYPE kafka_consumer_reply_queue gauge
kafka_consumer_reply_queue{client_id="avro-deserialiser-01",type="consumer"} 0.0
# HELP kafka_consumer_consumed_records_rate Average number of messages consumed (excluding ignored msgs) per second
# TYPE kafka_consumer_consumed_records_rate gauge
kafka_consumer_consumed_records_rate{client_id="avro-deserialiser-01",partition="0",topic="demo_data",type="consumer"} 458.01770895183716
kafka_consumer_consumed_records_rate{client_id="avro-deserialiser-01",partition="-1",topic="demo_data",type="consumer"} 0.0
# HELP kafka_consumer_consumed_bytes_rate Average message bytes (including framing) consumed per second
# TYPE kafka_consumer_consumed_bytes_rate gauge
kafka_consumer_consumed_bytes_rate{client_id="avro-deserialiser-01",partition="0",topic="demo_data",type="consumer"} 19236.74377597716
kafka_consumer_consumed_bytes_rate{client_id="avro-deserialiser-01",partition="-1",topic="demo_data",type="consumer"} 0.0
# HELP kafka_consumer_records_lag Number of messages consumer is behind producer on this partition
# TYPE kafka_consumer_records_lag gauge
kafka_consumer_records_lag{client_id="avro-deserialiser-01",partition="0",topic="demo_data",type="consumer"} 46.0
kafka_consumer_records_lag{client_id="avro-deserialiser-01",partition="-1",topic="demo_data",type="consumer"} -1.0
# HELP kafka_producer_reply_queue Number of ops(callbacks, events, etc) waiting in queue to serve with poll
# TYPE kafka_producer_reply_queue gauge
# HELP kafka_producer_queue_msg_cnt Current number of messages in prometheus_kafka_producer queues
# TYPE kafka_producer_queue_msg_cnt gauge
# HELP kafka_producer_queue_msg_size Current total size of messages in prometheus_kafka_producer queues
# TYPE kafka_producer_queue_msg_size gauge
# HELP kafka_producer_inflight_msg_cnt Number of messages in-flight to broker awaiting response
# TYPE kafka_producer_inflight_msg_cnt gauge
# HELP kafka_producer_queue_latency_avg Average Producer queue latency in milliseconds
# TYPE kafka_producer_queue_latency_avg gauge
# HELP kafka_producer_broker_latency_avg Broker latency / round-trip time in milliseconds
# TYPE kafka_producer_broker_latency_avg gauge
# HELP kafka_producer_batch_size_bytes_avg Average Batch sizes in bytes
# TYPE kafka_producer_batch_size_bytes_avg gauge
# HELP kafka_producer_batch_size_avg Average Batch message counts
# TYPE kafka_producer_batch_size_avg gauge
# HELP kafka_producer_request_rate Average number of requests sent per second
# TYPE kafka_producer_request_rate gauge
# HELP kafka_producer_request_bytes_rate Average number of requests bytes sent per second
# TYPE kafka_producer_request_bytes_rate gauge
# HELP kafka_producer_response_rate Average number of responses received per second
# TYPE kafka_producer_response_rate gauge
# HELP kafka_producer_response_bytes_rate Average number of response bytes received per second
# TYPE kafka_producer_response_bytes_rate gauge
```

## External References
Check out [Confluent's Developer portal](https://developer.confluent.io), it has free courses, documents, articles, blogs, podcasts and so many more content to get you up and running with a fully managed Apache Kafka service.

Disclaimer: I work for Confluent :wink:
