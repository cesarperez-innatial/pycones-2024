# STEP 1

## Scenario

Example producing messages to specific partitions:

* **Topic**: `pycones-attendees-new-4`
* **Partitions**: `3`

## Purpose

This demo aims to show how Kafka partitions management can help to keep a logic order on messages.

## Characteristics

* Producer: Produces a message every second
* Consumer: Takes 0.5 seconds to process a message

## Execution

* Create topic

  ```
  python prepare-env.py
  ```

  This command will create a topic named `pycones-attendees-new-4` with one partition

* Start consuming

  ```
  python consumer.py
  ```

  Consumer will connect to Kafka to subscribe to topic `pycones-attendees-new-4`

* Start producing

  ```
  python producer.py
  ```

  Producer will connect to Kafka sending messages to topic `pycones-attendees-new-4`. Consumer created in previous step will start consuming messages

* Observe message on each partition. They are perfectly ordered.

