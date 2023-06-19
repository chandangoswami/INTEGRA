const { Kafka } = require('kafkajs');
const flow_meta = require('./flowMetaFormat');

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
      //messages: [
      //  { value: 'Hello Kafka!' },
      //  { value: 'This is a message from the Kafka producer.' },
     // ],
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

//console.log(flow_meta) ;

runProducer().catch((error) => console.error('Producer error:', error));
