from kafka import KafkaConsumer

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    'fe-request',         # Specify the topic to consume from
    bootstrap_servers='BRO1:9092',   # Specify the Kafka broker(s)
    group_id='fe-request',       # Specify the consumer group
    auto_offset_reset='earliest',          # Start consuming from the beginning of the topic
    enable_auto_commit=True,               # Automatically commit offsets
    value_deserializer=lambda x: x.decode('utf-8')   # Deserialize message values as UTF-8 strings
)

# Start consuming messages
for message in consumer:
    # Extract the message key and value
    key = message.key
    value = message.value
    
    # Process the message
    print(f'Received message: Key={key}, Value={value}')
    
    # Perform additional processing or business logic here

