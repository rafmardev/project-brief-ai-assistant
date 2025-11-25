from core.interfaces.event_bus import EventBus
from infrastructure.events.kafka_event_bus import KafkaEventBus
from infrastructure.gemini.gemini_uploader_dummy import GeminiUploaderDummy
from core.use_cases.notify_gemini import NotifyGeminiUseCase

import time

def main():
    event_bus = KafkaEventBus(bootstrap_servers='localhost:9092', group_id='my-group')

    gemini_uploader = GeminiUploaderDummy()
    use_case = NotifyGeminiUseCase(gemini_uploader)

    def handle_event(data):
        use_case.notify(data)
    event_bus.subscribe("gemini_event", handle_event)

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()