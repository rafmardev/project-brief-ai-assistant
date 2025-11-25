from abc import ABC, abstractmethod

class EventBus(ABC):
    @abstractmethod
    def publish(self, event: str, data: dict) -> None:
        """Publishes an event to the event bus."""
        pass
    @abstractmethod 
    def subscribe(self, event: str, handler: callable) -> None:
        """Subscribes a handler to an event."""
        pass