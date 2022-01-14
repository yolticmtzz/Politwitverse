# import asyncio
# from azure.eventhub.aio import EventHubProducerClient
# from azure.eventhub import EventData

# async def run():
#     # Create a producer client to send messages to the event hub.
#     # Specify a connection string to your event hubs namespace and
#     # the event hub name.
#     producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://ns-politwit.servicebus.windows.net/;SharedAccessKeyName=socialtwitter-access;SharedAccessKey=CSE3VUIonXbWO2mbsEifircHmznPhlPVbulKKJ5AA7A=;EntityPath=socialtwitter-eh", eventhub_name="socialtwitter-eh")
#     async with producer:
#         # Create a batch.
#         event_data_batch = await producer.create_batch()

<<<<<<< HEAD
#         # Add events to the batch.
#         event_data_batch.add('joecl')
#         #event_data_batch.add('{"author_id": "3507009554","id": "1481684676720803843","text": "RT @nhbaptiste: this tweet is designed to get conservatives moralizing about crime so it conveniently leaves out that 301 of those officers…","source": "Twitter for iPhone"}')
=======
        # Add events to the batch.
        event_data_batch.add('{"author_id": "3507009554","id": "1481684676720803843","text": "RT @nhbaptiste: this tweet is designed to get conservatives moralizing about crime so it conveniently leaves out that 301 of those officers…","source": "Twitter for iPhone"}')
>>>>>>> f3dc4670e6a5048f64d7832021e64d0d0e851cd8

             
#         # Send the batch of events to the event hub.
#         await producer.send_batch(event_data_batch)

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run())

import time
import os
import uuid
import datetime
import random
import json

from azure.eventhub import EventHubProducerClient, EventData

# This script simulates the production of events for 10 devices.
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

# Create a producer client to produce and publish events to the event hub.
#producer = EventHubProducerClient.from_connection_string(conn_str="EVENT HUBS NAMESAPCE CONNECTION STRING", eventhub_name="EVENT HUB NAME")
producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://ns-politwit.servicebus.windows.net/;SharedAccessKeyName=socialtwitter-access;SharedAccessKey=CSE3VUIonXbWO2mbsEifircHmznPhlPVbulKKJ5AA7A=;EntityPath=socialtwitter-eh", eventhub_name="socialtwitter-eh")


for y in range(0,20):    # For each device, produce 20 events. 
    event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later. 
    for dev in devices:
        # Create a dummy reading.
        reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'uv': random.random(), 'temperature': random.randint(70, 100), 'humidity': random.randint(70, 100)}
        s = json.dumps(reading) # Convert the reading into a JSON string.
        event_data_batch.add(EventData(s)) # Add event data to the batch.
    producer.send_batch(event_data_batch) # Send the batch of events to the event hub.

# Close the producer.    
producer.close()
