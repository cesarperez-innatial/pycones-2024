import time
import datetime
import json
import namer
import random
from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9093",
                     "security.protocol": "PLAINTEXT"})

DOORS = 3
count = [0] * DOORS

running = True
while running:
    try:
        door = random.randint(0, DOORS - 1)
        count[door] += 1
        message = {'door': door,
                   'count': count[door],
                   'name': namer.generate(category='computer_science', style='title', separator=' '),
                   'datetime': datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S%z")}
        print(message)

        producer.produce(topic="pycones-attendees-new-4",
                         partition=door,
                         value=json.dumps(message))
        time.sleep(1)
    except KeyboardInterrupt:
        running = False

print("Flushing")
producer.flush()