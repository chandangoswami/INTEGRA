const { Kafka } = require('kafkajs');
//const flow_meta = require('./flowMetaFormat');
const flow_meta = require('./flowMetaFormat_input');

const kafka = new Kafka({
  clientId: 'fe-request',
  brokers: ['BRO1:9092'], // Replace with your Kafka broker(s) address
});

const producer = kafka.producer();

async function runProducer() {
  // Connect to the Kafka broker(s)
  await producer.connect();

  try {
    // Create a message object with the desired topic and payload
    const message = {
      topic: 'fe-request' ,
      messages: [
        { value: JSON.stringify(flow_meta )  }, 
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

runProducer().catch((error) => console.error('Producer error:', error));
