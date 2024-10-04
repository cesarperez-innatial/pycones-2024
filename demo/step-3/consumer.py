import sys
import time
from confluent_kafka import Consumer

if len(sys.argv) != 2:
    print("Exactly one argument expected (consumer group subfix)")
    exit(-1)

consumer_group_subfix = sys.argv[1]
consumer = Consumer({"bootstrap.servers": "localhost:9093",
                     "security.protocol": "PLAINTEXT",
                     "group.id": f"pycones.demo.{consumer_group_subfix}",
                     "auto.offset.reset": "earliest",
                     "enable.auto.commit": "true"})

consumer.subscribe( [ "pycones-attendees-new-3" ] )

running = True
while running:
    try:
        message = consumer.poll(1)
        if message is not None:
            print("-"*40)
            print(message.value().decode('utf-8'))
            print("Processing")
            # Mock processing time
            time.sleep(0.5)
            print("Processed")
    except KeyboardInterrupt:
        running = False
