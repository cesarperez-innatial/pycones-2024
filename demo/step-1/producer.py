import time
import datetime
import json
import namer
from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9093",
                     "security.protocol": "PLAINTEXT"})
count = 0
running = True
while running:
    try:
        count += 1
        message = {'count': count,
                   'name': namer.generate(category='computer_science', style='title', separator=' '),
                   'datetime': datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%S%z")}
        print(message)

        producer.produce(topic="pycones-attendees-new-1",
                         value=json.dumps(message))
        time.sleep(1)
    except KeyboardInterrupt:
        running = False

print("Flushing")
producer.flush()