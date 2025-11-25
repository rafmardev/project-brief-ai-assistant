from infrastructure.events.kafka_event_bus import KafkaEventBus
from infrastructure.gemini.gemini_uploader_dummy import GeminiUploaderDummy
from core.use_cases.notify_gemini import NotifyGeminiUseCase
from config.settings import get_settings

import time

def main():
    settings = get_settings()
    event_bus = KafkaEventBus(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS, group_id=settings.KAFKA_GROUP_ID)

    gemini_uploader = GeminiUploaderDummy()
    use_case = NotifyGeminiUseCase(gemini_uploader)

    def handle_event(data):
        use_case.notify(data)
    event_bus.subscribe("gemini_event", handle_event)

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()