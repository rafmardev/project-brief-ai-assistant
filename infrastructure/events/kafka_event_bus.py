from confluent_kafka import Producer, Consumer, KafkaError
import json
import threading

from core.interfaces.event_bus import EventBus

class KafkaEventBus(EventBus):
    def __init__(self, bootstrap_servers: str, group_id: str):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.bootstrap_servers = bootstrap_servers
        self.group_id = group_id
        pass
    def publish(self, topic: str, data: dict) -> None:
        data = json.dumps(data).encode('utf-8')
        self.producer.produce(topic, data)
        self.producer.flush()
        """Publishes an event to the Kafka event bus."""

    def subscribe(self, event: str, handler: callable) -> None:
        """Subscribes a handler to a Kafka event."""

        def listen():
            consumer = Consumer({
                'bootstrap.servers': self.bootstrap_servers,
                'group.id': self.group_id,
                'auto.offset.reset': 'earliest'
            })

            consumer.subscribe([event])

            while True:
                msg = consumer.poll(1.0)

                if msg is None:
                    continue
                if msg.error():
                    if msg.error():
                        raise KafkaError(msg.error())
                else:
                    data = json.loads(msg.value().decode('utf-8'))
                    handler(data)
        thread = threading.Thread(target=listen, daemon=True)
        thread.start()