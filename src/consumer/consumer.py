from azure.eventhub import EventHubConsumerClient
import json
import os

EVENT_HUB_CONNECTION_STRING = os.getenv("EVENT_HUB_CONNECTION_STRING")
event_hub_name = "stock-data"

client = EventHubConsumerClient.from_connection_string(EVENT_HUB_CONNECTION_STRING, consumer_group="$Default", eventhub_name=event_hub_name)

def on_event(partition_context, event):
    data = json.loads(event.body_as_str())
    print(f"Received event: {data}")
    partition_context.update_checkpoint(event)

with client:
    client.receive(on_event, starting_position="-1")  # From the beginning