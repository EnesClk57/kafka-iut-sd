from kafka import KafkaProducer
import json
from datetime import datetime
import time

# Define the Kafka broker and topic
broker = 'kafka.e44394u-dev.svc.cluster.local:9092'
topic = 'my-first-topic'

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[broker],
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_PLAINTEXT',
    sasl_plain_username='user1',
    sasl_plain_password='VoXRSLWisf',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

i = 0

while True:
    message = {
        'key': 'consumer_instances',
        'value': 3,
        'timestamp': int(time.time())
    }
    
    # Send the message to the Kafka topic
    producer.send(topic, partition=0, value=message)

    # Ensure all messages are sent before waiting
    producer.flush()

    print(f"Message envoyé à {topic}")
    time.sleep(1)