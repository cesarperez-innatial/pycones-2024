from confluent_kafka.admin import AdminClient, NewTopic


admin_client = AdminClient({
    "bootstrap.servers": "localhost:9093",
    "security.protocol": "PLAINTEXT"
})

fs = admin_client.create_topics([ NewTopic("pycones-attendees-new-1",
                                            num_partitions=1,
                                            replication_factor=1) ] )
for topic, f in fs.items():
    try:
        f.result()
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))