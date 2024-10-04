import time
from confluent_kafka import Consumer

consumer = Consumer({"bootstrap.servers": "localhost:9093",
                     "security.protocol": "PLAINTEXT",
                     "group.id": "pycones.demo",
                     "auto.offset.reset": "earliest",
                     "enable.auto.commit": "true"})

consumer.subscribe( [ "pycones-attendees-new-2" ] )

running = True
while running:
    try:
        message = consumer.poll(1)
        if message is not None:
            print("-"*40)
            print(message.value().decode('utf-8'))
            print("Processing")
            # Mock processing time
            time.sleep(1.5)
            print("Processed")
    except KeyboardInterrupt:
        running = False
