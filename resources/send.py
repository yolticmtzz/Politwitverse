import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://ns-politwit.servicebus.windows.net/;SharedAccessKeyName=socialtwitter-access;SharedAccessKey=CSE3VUIonXbWO2mbsEifircHmznPhlPVbulKKJ5AA7A=;EntityPath=socialtwitter-eh", eventhub_name="socialtwitter-eh")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(''
        {
            "author_id": "3507009554",
            "id": "1481684676720803843",
            "text": "RT @nhbaptiste: this tweet is designed to get conservatives moralizing about crime so it conveniently leaves out that 301 of those officers…",
            "source": "Twitter for iPhone"
        }'

             
        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
