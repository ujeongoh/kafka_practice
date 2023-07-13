from time import sleep
from json import dumps
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x:dumps(x).encode('utf-8')
)

for j in range(99):
    print('Iteration')
    data = {'counter': j}
    producer.send('topic_test', value=data)
    sleep(0.5)