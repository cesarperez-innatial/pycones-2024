# PyConEs 2024

## Apache Kafka with Python (Examples)

* Requirements

  This demo is supposed to work with python >=3.11. If you use previous versions, you will find problems with `datetime.UTC` usage, (due it was introduced in python `3.11`). If you want to use previous versions you can replace

  ```python
  datetime.datetime.now(datetime.UTC)
  ```

  by

  ```python
  datetime.datetime.utcnow()
  ```

* Prepare the environment installing dependencies

  ```
  pip install -r requirements.txt
  ```

  Navigate through different demo steps:

  * [Step-1](step-1): Usecase having one producer and one consumer. Kafka topic with only one partition.
  * [Step-2](step-2): Usecase having one producer and more than one consumer belonging to same consumer group. Kafka topic having more than one partition.
  * [Step-3](step-3): Usecase having one producer and more than one consumer belonging to different consumer groups.
  * [Step-4](step-4): Usecase having one producer sending messages to specific partitions.
