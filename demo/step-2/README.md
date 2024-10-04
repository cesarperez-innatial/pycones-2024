# STEP 2

## Scenario

Example having multiples comsumers with same consumer group `pycones.demo`:

* **Topic**: `pycones-attendees-new-2`
* **Partitions**: `2`

## Purpose

This demo aims to show how Kafka can distribute messages among several consumers (having same consumer group).

## Characteristics

* Producer: Produces a message every second
* Consumer: Takes 1.5 seconds to process a message

## Execution

* Create topic

  ```
  python prepare-env.py
  ```

  This command will create a topic named `pycones-attendees-new-2` with two partitions

* Start consuming

  ```
  python consumer.py
  ```

  Consumer will connect to Kafka to subscribe to topic `pycones-attendees-new-2`

* Start producing

  ```
  python producer.py
  ```

  Producer will connect to Kafka sending messages to topic `pycones-attendees-new-2`. Consumer created in previous step will start consuming messages

* Start seconds consumer

  ```
  python consumer.py
  ```

  Consumer will connect to Kafka to subscribe to topic `pycones-attendees-new-2`. Kafka will rebalance partitions among both consumers