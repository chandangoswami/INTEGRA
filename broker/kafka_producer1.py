from confluent_kafka import Producer, KafkaError

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'Python_produces'
}

# Create a Kafka producer instance
producer = Producer(conf)

# Define the topic to which you want to publish messages
topic = 'quickstart-events'

# Publish messages
messages = [
    'Message 1',
    'Message 2',
    'Message 3'
]

def delivery_callback(err, msg):
    if err:
        print(f'Failed to deliver message: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

for message in messages:
    # Produce the message and send it to the topic
    producer.produce(topic, message, callback=delivery_callback)

# Wait for the messages to be delivered
producer.flush()

# Close the producer connection
producer.close()

