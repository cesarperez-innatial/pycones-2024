# STEP 1

## Scenario

Basic example of production and consumption:

* **Topic**: `pycones-attendees-new-1`
* **Partitions**: `1`

## Purpose

This demo aims to show how Kafka topic can be used a simple FIFO queue.

## Characteristics

* Producer: Produces a message every second
* Consumer: Takes 0.5 seconds to process a message

## Execution

* Create topic

  ```
  python prepare-env.py
  ```

  This command will create a topic named `pycones-attendees-new-1` with one partition

* Start consuming

  ```
  python consumer.py
  ```

  Consumer will connect to Kafka to subscribe to topic `pycones-attendees-new-1`

* Start producing

  ```
  python producer.py
  ```

  Producer will connect to Kafka sending messages to topic `pycones-attendees-new-1`. Consumer created in previous step will start consuming messages

