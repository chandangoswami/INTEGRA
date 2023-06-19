const { Kafka } = require('kafkajs');
const jsonData = require('./flowMetaFormat.json') ;

const kafka = new Kafka({
  clientId: 'my-kafka-producer',
  brokers: ['BRO1:9092'], // Replace with your Kafka broker(s) address
});

const producer = kafka.producer();

async function runProducer() {
  // Connect to the Kafka broker(s)
  await producer.connect();

  try {
    // Create a message object with the desired topic and payload
	  

    const message = {
      topic: 'my-topic',
      messages: [
        { value: 'Hello Kafka!' },
        { value: jsonData },
      ],
    };

    // Send the message to the Kafka broker(s)
    await producer.send(message);

    console.log('Message sent successfully!');
  } catch (error) {
    console.error('Error sending message:', error);
  } finally {
    // Disconnect the producer
    await producer.disconnect();
  }
}

//console.log('JSON data:', jsonData );

runProducer().catch((error) => console.error('Producer error:', error));

