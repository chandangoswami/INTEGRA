from confluent_kafka import Consumer, KafkaError

# Kafka consumer configuration
conf = {
    'bootstrap.servers': 'BRO1:9092',  # Replace with your Kafka broker addresses
    'group.id': 'fe-request',       # Consumer group ID
    'auto.offset.reset': 'earliest'       # Start consuming from the beginning of the topic
}

# Create a Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to a Kafka topic
topic ='fe-request' # Replace with the topic you want to consume from
consumer.subscribe([topic])

try:
    while True:
        # Poll for new messages
        msg = consumer.poll(1.0)  # Adjust the timeout as needed

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print('Reached end of partition')
            else:
                print('Error: {}'.format(msg.error().str()))
        else:
            # Process the received message
            print('Received message: {}'.format(msg.value().decode('utf-8')))

except KeyboardInterrupt:
    pass

finally:
    # Close the consumer to release resources
    consumer.close()

