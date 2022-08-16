#!/usr/bin/env python
import time
import schedule
import random
import uuid
from kafka import KafkaProducer
from json import dumps  
import os

def get_data():

    # Producer instance
    my_data = {'temperature' : random.randint(1, 100), 'id' : str(uuid.uuid4())}
    brokers = os.environ.get('KAFKA_BROKERS').split(',')
    prod = KafkaProducer(bootstrap_servers=brokers,value_serializer = lambda x:dumps(x).encode('utf-8'))
    print(my_data)
    prod.send(topic='temperatures', value=my_data)
    prod.flush()

if __name__ == "__main__":

    get_data()
    schedule.every(5).seconds.do(get_data)

    while True:
        schedule.run_pending()
        time.sleep(1)