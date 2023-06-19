import json
import base64
from cryptography.fernet import Fernet
from confluent_kafka import Producer

# Kafka broker configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my_producer'
}

# Create a Kafka producer instance
producer = Producer(conf)

# Define the topic to which you want to publish messages
topic = 'your_topic_name'

# JSON object to send
json_data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Convert JSON object to JSON string
json_string = json.dumps(json_data)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt the JSON string
encrypted_data = cipher_suite.encrypt(json_string.encode('utf-8'))

# Serialize the encrypted data into a string format (Base64)
serialized_data = base64.b64encode(encrypted_data).decode('utf-8')

# Publish the encrypted message to the topic
producer.produce(topic, serialized_data)

# Wait for the message to be delivered
producer.flush()

# Close the producer connection
producer.close()

