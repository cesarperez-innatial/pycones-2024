# STEP 2

## Scenario

Example having multiples comsumers with same consumer group `pycones.demo`:

* **Topic**: `pycones-attendees-new-3`
* **Partitions**: `6`

## Purpose

This demo aims to show how Kafka can send same message to multiples consumers (having different consumer group).

## Characteristics

* Producer: Produces a message every second
* Consumer: Takes 0.5 seconds to process a message

## Execution

* Create topic

  ```
  python prepare-env.py
  ```

  This command will create a topic named `pycones-attendees-new-3` with two partitions

* Start consuming

  ```
  python consumer.py 1
  ```

  Consumer will connect to Kafka to subscribe to topic `pycones-attendees-new-3` using consumer group `pycones.demo.1`

* Start producing

  ```
  python producer.py
  ```

  Producer will connect to Kafka sending messages to topic `pycones-attendees-new-3`. Consumer created in previous step will start consuming messages

* Start seconds consumer with different consumer group

  ```
  python consumer.py 2
  ```

  Consumer will connect to Kafka to subscribe to topic `pycones-attendees-new-3` using consumer group `pycones.demo.2`. Consumer will receive message produced before be launched